from gptos.plugins.base import GPTOSPlugin
from gptos.system.plugin_loader import load_plugins

class ReloadPlugin(GPTOSPlugin):
    def register(self, context): pass

    def execute(self, command, context):
        load_plugins()
        print("🔁 Plugins reloaded.")

PLUGIN_REGISTRY = {
    "reload": ReloadPlugin()
}
