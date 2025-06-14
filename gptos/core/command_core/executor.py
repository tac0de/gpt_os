from gptos.system.plugin_loader import PLUGIN_REGISTRY
from gptos.system.ethics import ethics_guard
from gptos.system.command_log import logger

@ethics_guard
def execute(command, context):
    handler = PLUGIN_REGISTRY.get(command.name)
    raw_input = command.raw if hasattr(command, "raw") else str(command)
    
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