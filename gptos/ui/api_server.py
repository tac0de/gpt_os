from fastapi import FastAPI, Request
from pydantic import BaseModel
from gptos.system.context_handler import create_system_context
from gptos.core.command_core.executor import execute_command
from gptos.system.plugin_loader import load_plugins, PLUGIN_REGISTRY
from typing import List

app = FastAPI(title="GPT OS API", version="0.6.0")

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

# === Routes ===

@app.get("/status")
def get_status():
    return {
        "status": "ok",
        "loaded_plugins": list(context.plugins.keys()),
        "memory_length": len(context.memory),
        "version": "0.6.0"
    }

@app.post("/execute")
def execute(req: CommandRequest):
    result = execute_command(req.command, context)
    return {"input": req.command, "result": result}

@app.post("/rag")
def run_rag(req: RAGRequest):
    if not hasattr(context, "rag_pipeline"):
        return {"error": "RAG pipeline not initialized."}
    response = context.rag_pipeline.run(query=req.query)
    return {"query": req.query, "response": response}

@app.post("/rag/add")
def add_rag_docs(req: RAGAddRequest):
    if not hasattr(context, "rag_pipeline"):
        return {"error": "RAG pipeline not initialized."}
    
    context.rag_pipeline.add_documents(req.docs)
    return {"added": len(req.docs)}

@app.get("/rag/documents")
def list_rag_documents():
    if not hasattr(context, "rag_pipeline"):
        return {"error": "RAG pipeline not initialized."}
    return {"documents": context.rag_pipeline.documents}

@app.post("/rag/reset")
def reset_rag():
    if not hasattr(context, "rag_pipeline"):
        return {"error": "RAG pipeline not initialized."}
    
    count = len(context.rag_pipeline.documents)
    context.rag_pipeline.documents.clear()
    context.rag_pipeline.embeddings.clear()
    return {"reset": True, "count": count}

# ✅ Optional debug route
@app.get("/debug/plugins")
def list_plugins():
    return list(context.plugins.keys())
