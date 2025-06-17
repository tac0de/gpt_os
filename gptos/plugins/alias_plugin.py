# gptos/plugins/alias_plugin.py

import os
import json
from gptos.plugins.base import GPTOSPlugin
from gptos.system.alias_manager import AliasManager
from gptos.system.config_loader import get_alias_file_path

ALIAS_FILE_PATH = get_alias_file_path()

class AliasPlugin(GPTOSPlugin):
    name = "alias"

    def __init__(self):
        self.aliases = {}

    def register(self, context):
        if not hasattr(context, "alias_manager"):
            context.alias_manager = AliasManager()

    def execute(self, command, context):
        args = command.args
        if not args:
            print("Usage: alias [set name=value | list | export | import | add <name> <target>]")
            return

        # fallback
        if not hasattr(context, "alias_manager"):
            context.alias_manager = AliasManager()

        manager = context.alias_manager
        subcommand = args[0]

        if subcommand == "set":
            # join all remaining args for full value with spaces
            raw_assignment = " ".join(args[1:])
            if "=" in raw_assignment:
                name, value = raw_assignment.split("=", 1)
                manager.set_alias(name.strip(), value.strip())
                print(f"[alias] Set: {name.strip()} → {value.strip()}")

        elif subcommand == "list":
            aliases = manager.get_all()
            if not aliases:
                print("[alias] No aliases defined.")
            else:
                for name, val in aliases.items():
                    print(f"{name} = {val}")

        elif subcommand == "export":
            aliases = manager.get_all()
            try:
                os.makedirs(os.path.dirname(ALIAS_FILE_PATH), exist_ok=True)
                with open(ALIAS_FILE_PATH, "w", encoding="utf-8") as f:
                    json.dump(aliases, f, indent=2)
                print(f"[alias] Exported to {ALIAS_FILE_PATH}")
            except Exception as e:
                print(f"[alias] Export failed: {e}")

        elif subcommand == "import":
            try:
                with open(ALIAS_FILE_PATH, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for k, v in data.items():
                        manager.set_alias(k, v)
                print(f"[alias] Imported from {ALIAS_FILE_PATH}")
            except Exception as e:
                print(f"[alias] Import failed: {e}")

        elif subcommand == "add":
            self.handle_add(args[1:])

        else:
            print("Invalid alias command. Try: alias set ls=log search | alias list | alias export | alias import | alias add <name> <target>")

    def handle_add(self, args):
        if len(args) < 2:
            print("Usage: alias add <name> <target>")
            return

        alias_name = args[0]
        target = " ".join(args[1:])

        if " " in alias_name or " " in target:
            print("[alias] ❌ Cannot alias multi-word phrases. Only single command tokens allowed.")
            return

        self.aliases[alias_name] = target
        print(f"[alias] ✅ {alias_name} → {target}")


PLUGIN_REGISTRY = {
    "alias": AliasPlugin()
}
