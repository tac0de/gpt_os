from gptos.system.plugin_loader import PLUGIN_REGISTRY
from gptos.system.command_log import logger
from gptos.system.ethics import ethics_guard

@ethics_guard
def execute(command, context):
    raw_input = command.raw if hasattr(command, "raw") else str(command)

    # 🧩 Step 1: resolve alias
    resolved = context.alias_manager.resolve(command.name)
    if resolved:
        print(f"[alias] '{command.name}' → '{resolved}'")
        resolved_parts = resolved.strip().split()

        if resolved_parts:
            command.name = resolved_parts[0]                      # ✅ log
            command.args = resolved_parts[1:] + command.args      # ✅ ['search'] + existing args

    # 🧩 Step 2: find handler
    handler = PLUGIN_REGISTRY.get(command.name)

    try:
        if handler:
            result = handler.execute(command, context)
            logger.log(raw_input, parsed=vars(command), result=result)
            return result
        else:
            logger.log(raw_input, parsed=vars(command), error=Exception("Unknown command"))
            print(f"Unknown command: {command.name}")
    except Exception as e:
        logger.log(raw_input, parsed=vars(command), error=e)
        raise
