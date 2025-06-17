import importlib
import sys
import os

from gptos.plugins.base import GPTOSPlugin
from gptos.system.plugin_loader import load_plugins, PLUGIN_REGISTRY

class ReloadPlugin(GPTOSPlugin):
    name = "reload"

    def register(self, context):
        pass

    def execute(self, command, context):
        args = command.args
        if not args:
            print("Usage: reload <plugin_name|all>")
            return

        args = command.args
        if not args or args[0] == "all":
            print("[reload] Reloading all plugins...")
            load_plugins()
            print(f"[PLUGIN LOADER] ✅ Loaded: {list(PLUGIN_REGISTRY.keys()) or 'none'}")
        else:
            print(f"[reload] Selective reload not supported. Use `reload all` for now.")


PLUGIN_REGISTRY["reload"] = ReloadPlugin()