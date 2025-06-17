# plugin_loader.py

import importlib
import gptos.plugins as plugins
import sys
import os

PLUGIN_REGISTRY = {}  # This must NEVER be reassigned after this line

def load_plugins():
    # ✅ Only clear and update, DO NOT reassign
    PLUGIN_REGISTRY.clear()

    plugin_dir = os.path.dirname(plugins.__file__)
    loaded = []

    for filename in os.listdir(plugin_dir):
        if filename.endswith("_plugin.py"):
            module_name = filename[:-3]
            module_path = f"{plugins.__name__}.{module_name}"
            try:
                if module_path in sys.modules:
                    importlib.reload(sys.modules[module_path])
                else:
                    importlib.import_module(module_path)
                mod = sys.modules[module_path]
                if hasattr(mod, "PLUGIN_REGISTRY"):
                    PLUGIN_REGISTRY.update(mod.PLUGIN_REGISTRY)
                    loaded.extend(mod.PLUGIN_REGISTRY.keys())
                else:
                    print(f"[SKIPPED] {module_name} has no PLUGIN_REGISTRY")
            except Exception as e:
                print(f"[ERROR] Failed to load {module_name}: {e}")
