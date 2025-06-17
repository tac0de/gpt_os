from fastapi import FastAPI, HTTPException
import importlib
from pydantic import BaseModel
from gptos.system.context_handler import create_system_context
from gptos.core.command_core.executor import execute_command
from gptos.system.plugin_loader import load_plugins, PLUGIN_REGISTRY
from gptos.system.rag_pipeline import SimpleRAGPipeline  # RAG 파이프라인을 불러옵니다
from typing import List
from gptos.system.command_log import logger
import time
import cachetools

app = FastAPI(title="GPT OS API", version="0.6.1")
# === Rate Limiting Cache ===
rate_limit_cache = cachetools.TTLCache(maxsize=1000, ttl=60)  # TTL 60초, 최대 1000개 키 저장

# === Startup ===
context = create_system_context()
load_plugins()
context.plugins = PLUGIN_REGISTRY  # ❗️핵심

# === Models ===

class CommandRequest(BaseModel):
    command: str

class RAGRequest(BaseModel):
    query: str
class RAGAddRequest(BaseModel):
    docs: List[str]

# === Helper Function ===
def check_rate_limit(ip: str):
    """IP별 요청 빈도 체크"""
    now = time.time()
    if ip in rate_limit_cache:
        last_request_time = rate_limit_cache[ip]
        if now - last_request_time < 1:  # 1초 이상 차이날 경우 요청 허용
            raise HTTPException(status_code=429, detail="Rate limit exceeded")
    rate_limit_cache[ip] = now


# === Routes ===

@app.get("/status")
async def get_status():
    return {
        "status": "ok",
        "loaded_plugins": list(context.plugins.keys()),
        "memory_length": len(context.memory),
        "version": "0.6.0"
    }

@app.post("/execute")
async def execute(req: CommandRequest):
    result = await execute_command(req.command, context)
    return {"input": req.command, "result": result}

@app.post("/rag")
async def run_rag(req: RAGRequest):
    # 비동기 처리 및 RAG 성능 최적화
    if not hasattr(context, "rag_pipeline"):
        return {"error": "RAG pipeline not initialized."}
    response = await context.rag_pipeline.run(req.query)  # 비동기 방식으로 처리
    return {"query": req.query, "response": response}

@app.post("/rag/add")
async def add_rag_docs(req: RAGAddRequest):
    """RAG 파이프라인에 문서 추가"""
    if not hasattr(context, "rag_pipeline") or context.rag_pipeline is None:
        context.rag_pipeline = SimpleRAGPipeline()  # 자동 초기화
        return {"message": "RAG pipeline was initialized automatically."}
    
    context.rag_pipeline.add_documents(req.docs)
    return {"added": len(req.docs)}

@app.get("/rag/documents")
async def list_rag_documents():
    """등록된 문서 목록 조회"""
    if not hasattr(context, "rag_pipeline") or context.rag_pipeline is None:
        context.rag_pipeline = SimpleRAGPipeline()  # 자동 초기화
        return {"message": "RAG pipeline was initialized automatically."}
    
    return {"documents": context.rag_pipeline.documents}

# gptos/ui/api_server.py
@app.get("/plugins")
async def list_plugins():
    return {"plugins": list(PLUGIN_REGISTRY.keys())}


# 플러그인 추가 API
@app.post("/plugins/add")
async def add_plugin(plugin_name: str):
    """플러그인 추가"""
    try:
        # 플러그인 모듈을 동적으로 로드
        plugin_module = importlib.import_module(f"gptos.plugins.{plugin_name}")
        
        # PLUGIN_REGISTRY에 플러그인 등록
        if hasattr(plugin_module, "PLUGIN_REGISTRY"):
            context.plugins.update(plugin_module.PLUGIN_REGISTRY)
        else:
            raise HTTPException(status_code=400, detail=f"Plugin {plugin_name} does not have a valid PLUGIN_REGISTRY.")
        
        return {"message": f"Plugin {plugin_name} added successfully."}
    except ModuleNotFoundError:
        raise HTTPException(status_code=404, detail=f"Plugin {plugin_name} not found.")

# 플러그인 삭제 API
@app.post("/plugins/remove")
async def remove_plugin(plugin_name: str):
    """플러그인 삭제"""
    if plugin_name in context.plugins:
        del context.plugins[plugin_name]
        return {"message": f"Plugin {plugin_name} removed successfully."}
    else:
        raise HTTPException(status_code=404, detail=f"Plugin {plugin_name} not found.")


@app.get("/system/config")
async def get_system_config():
    """시스템 설정 정보 반환"""
    config = {
        "strict_mode": context.config.get("strict_mode", True),
        "log_level": context.config.get("log.level", "INFO"),
        "memory_deduplication": context.config.get("memory.dedup", True),
        "summarize_recent_count": context.config.get("summarize.recent_count", 10),
    }
    return {"config": config}


@app.get("/system/status")
async def get_system_status():
    """시스템 상태 반환"""
    return {
        "status": "ok",
        "loaded_plugins": len(context.plugins),
        "memory_length": len(context.memory),
        "version": "0.6.0"
    }

@app.get("/system/optimize")
async def optimize_system():
    """메모리 최적화 수행"""
    context.optimize_memory()
    context.clean_old_data()  # 오래된 데이터 삭제
    return {"status": "memory optimized"}


@app.get("/debug/plugins")
async def list_plugins():
    """디버깅용 플러그인 목록 조회"""
    return {"plugins": list(context.plugins.keys())}

# API 호출 로그 기록
def api_call_log(endpoint: str, response_status: str):
    logger.info(f"API call: {endpoint}, Response Status: {response_status}")