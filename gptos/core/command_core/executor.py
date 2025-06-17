# gptos/core/command_core/executor.py

from gptos.system.plugin_loader import PLUGIN_REGISTRY
from gptos.system.command_log import logger
from gptos.system.ethics import ethics_guard
import time

@ethics_guard
def execute(command, context):
    raw_input = command.raw if hasattr(command, "raw") else str(command)

    # 🧩 Step 1: resolve alias
    resolved = context.alias_manager.resolve(command.name)
    if resolved:
        print(f"[alias] '{command.name}' → '{resolved}'")
        resolved_parts = resolved.strip().split()
        if resolved_parts:
            command.name = resolved_parts[0]
            command.args = resolved_parts[1:] + command.args

    # 🧩 Step 2: find handler
    handler = PLUGIN_REGISTRY.get(command.name)

    start_time = time.time()
    result = None
    error = None
    plugin_name = command.name
    status = "OK"

    try:
        if handler:
            result = handler.execute(command, context)
        else:
            raise Exception("Unknown command")
    except Exception as e:
        error = e
        status = "ERROR"
        print(f"[ERROR] {e}")
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

    if error:
        raise error
    return result
