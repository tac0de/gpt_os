import asyncio
import time
from gptos.system.plugin_loader import PLUGIN_REGISTRY
from gptos.system.command_log import logger
from gptos.system.ethics import ethics_guard
from gptos.core.command_core.parser import parse_command
from functools import lru_cache

# 비동기 명령어 처리 함수
async def execute_command_async(command, context):

    raw_input = command.raw if hasattr(command, "raw") else str(command)

    # 🧩 Step 1: resolve alias
    resolved = context.alias_manager.resolve(command.name)
    if resolved:
        print(f"[alias] '{command.name}' → '{resolved}'")
        resolved_parts = resolved.strip().split()
        if resolved_parts:
            command.name = resolved_parts[0]
            command.args = resolved_parts[1:] + command.args
        logger.info(f"Alias resolved: {command.name} → {resolved}")

    # 🧩 Step 2: check if it's a RAG command
    if command.name == "rag":
        # RAG 명령어 실행 최적화
        query = command.args[0] if command.args else ""
        result = context.rag_pipeline.run(query)
        return result


    # 🧩 Step 3: find handler
    handler = PLUGIN_REGISTRY.get(command.name)

    start_time = time.time()
    result = None
    error = None
    plugin_name = command.name
    status = "OK"

    try:
        if handler:
            result = await handler.execute(command, context)  # 비동기 실행
        else:
            raise Exception("Unknown command")
    except Exception as e:
        error = e
        status = "ERROR"
        logger.error(f"Error executing {command.name}: {e}")
    finally:
        duration = round(time.time() - start_time, 4)
        logger.log(
            raw_input=raw_input,
            parsed=vars(command),
            result=result,
            error=error,
            status=status,
            duration=duration,
            plugin=plugin_name,
        )
        logger.info(f"Execution finished for {command.name} in {duration} seconds")

    if error:
        raise error
    return result

# 비동기 명령어 실행을 위한 래퍼
async def execute(command, context):
    return await execute_command_async(command, context)

# 캐시된 명령어 실행 (자주 호출되는 결과를 저장)
@lru_cache(maxsize=100)
def cached_execute_command(command_str: str, context):
    """캐시된 명령어 실행"""
    command = parse_command(command_str, context)
    return execute(command, context)

def execute_command(command_str: str, context):
    """외부 인터페이스에서 호출되는 명령어 실행 (비동기 처리)"""
    return asyncio.run(cached_execute_command(command_str, context))  # 캐시된 명령어 처리
