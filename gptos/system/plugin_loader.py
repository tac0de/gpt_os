import os
import importlib.util
import inspect

class PluginLoader:
    def __init__(self, plugin_dir):
        self.plugin_dir = os.path.abspath(plugin_dir)
        self.commands = {}
        self.load_plugins()

    def load_plugins(self):
        if not os.path.isdir(self.plugin_dir):
            print(f"[DEBUG] Plugin path: {self.plugin_dir}, exists: False")
            return
        for file in os.listdir(self.plugin_dir):
            if file.endswith(".py") and not file.startswith("__"):
                path = os.path.join(self.plugin_dir, file)
                name = os.path.splitext(file)[0]
                spec = importlib.util.spec_from_file_location(name, path)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                if hasattr(mod, "get_commands"):
                    self.commands.update(mod.get_commands())

    def resolve(self, cmd):
        return self.commands.get(cmd)

    def is_async(self, cmd):
        func = self.commands.get(cmd)
        return inspect.iscoroutinefunction(func)
