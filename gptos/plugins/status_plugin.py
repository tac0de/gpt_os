from gptos.system.plugin_loader import PLUGIN_REGISTRY

def status_command(command, context):
    return {
        "status": "ok",
        "loaded_plugins": list(context.plugins.keys()),
        "memory_length": len(context.memory),
        "version": "0.6.0"
    }

PLUGIN_REGISTRY = {
    "status": type("SimplePlugin", (), {"execute": staticmethod(status_command)})()
}
