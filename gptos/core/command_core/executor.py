from gptos.system.plugin_loader import PLUGIN_REGISTRY
from gptos.system.ethics import ethics_guard

@ethics_guard
def execute(command, context):
    handler = PLUGIN_REGISTRY.get(command.name)
    if handler:
        return handler.execute(command, context)
    print(f"Unknown command: {command.name}")
