from gptos.plugins.base import GPTOSPlugin
import sys

class StatusPlugin(GPTOSPlugin):
    def register(self, context): pass

    def execute(self, command, context):
        # 🔁 Dynamic import of latest plugin registry
        plugin_loader = sys.modules.get("gptos.system.plugin_loader")
        plugin_registry = plugin_loader.PLUGIN_REGISTRY if plugin_loader else {}

        print("🧭 GPT OS STATUS")
        print(f"Ethics Mode: {'ON ✅' if context.config.get('strict_mode') else 'OFF ❌'}")
        print(f"Loaded Plugins: {len(plugin_registry)}")
        print(" - " + ", ".join(sorted(plugin_registry.keys())))
        print(f"Memory Length: {len(context.memory)}")

# ✅ MUST be at global scope
PLUGIN_REGISTRY = {
    "status": StatusPlugin()
}