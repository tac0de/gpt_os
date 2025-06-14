from gptos.plugins.base import GPTOSPlugin
import os
import platform
import subprocess

class GeneratePlugin(GPTOSPlugin):
    name = "generate"

    def register(self, context): pass

    def execute(self, command, context):
        if not command.args or command.args[0] != "plugin":
            print("Usage: generate plugin <plugin_name> [--with-tests] [--open]")
            return

        plugin_name = command.args[1]
        class_name = plugin_name.capitalize() + "Plugin"
        filename = f"{plugin_name}_plugin.py"
        filepath = os.path.join("gptos", "plugins", filename)

        with_tests = "--with-tests" in command.args
        open_after = "--open" in command.args

        if os.path.exists(filepath):
            print(f"[generate] Plugin already exists: {filepath}")
        else:
            code = f'''from gptos.plugins.base import GPTOSPlugin

class {class_name}(GPTOSPlugin):
    name = "{plugin_name}"

    def register(self, context): pass

    def execute(self, command, context):
        print("[{plugin_name}] Plugin activated.")
        print("Command args:", command.args)

PLUGIN_REGISTRY = {{
    "{plugin_name}": {class_name}()
}}
'''
            with open(filepath, 'w') as f:
                f.write(code)
            print(f"[generate] Created plugin: {filepath}")

        if with_tests:
            test_dir = os.path.join("tests")
            os.makedirs(test_dir, exist_ok=True)
            test_path = os.path.join(test_dir, f"test_{plugin_name}_plugin.py")
            if not os.path.exists(test_path):
                with open(test_path, 'w') as f:
                    f.write(f'''import pytest

def test_{plugin_name}_basic():
    assert True  # TODO: Replace with real test
''')
                print(f"[generate] Created test: {test_path}")
            else:
                print(f"[generate] Test already exists: {test_path}")

        if open_after:
            open_path = filepath
            cmd = ["code", open_path] if platform.system() == "Darwin" or platform.system() == "Linux" else ["start", open_path]
            try:
                subprocess.run(cmd, check=False)
            except Exception as e:
                print(f"[generate] Failed to open file: {e}")


PLUGIN_REGISTRY = {
    "generate": GeneratePlugin()
}