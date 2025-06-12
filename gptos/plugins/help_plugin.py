from gptos.plugins.base import GPTOSPlugin
import sys

class HelpPlugin(GPTOSPlugin):
    def register(self, context): pass

    def execute(self, command, context):
        plugin_loader = sys.modules.get("gptos.system.plugin_loader")
        registry = plugin_loader.PLUGIN_REGISTRY if plugin_loader else {}

        print("📘 GPT OS COMMANDS")
        for name in sorted(registry.keys()):
            print(f" - {name}")

        print("\nUse `config`, `alias`, `status`, `memory`, `reload`, etc.")

PLUGIN_REGISTRY = {
    "help": HelpPlugin()
}
