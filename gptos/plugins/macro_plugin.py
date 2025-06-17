from gptos.plugins.base import GPTOSPlugin
from gptos.core.command_core.parser import parse_command
from gptos.core.command_core.executor import execute as run_command

class MacroPlugin(GPTOSPlugin):
    name = "macro"

    def __init__(self):
        self.macros = {}

    def register(self, context):
        # 옵션: 향후 파일 기반 저장/로드 가능
        pass

    def execute(self, command, context):
        args = command.args
        if not args:
            print("Usage: macro [save|run|list|delete] ...")
            return

        subcmd = args[0]

        if subcmd == "save" and len(args) >= 3:
            name = args[1]
            raw_sequence = " ".join(args[2:])
            commands = [cmd.strip() for cmd in raw_sequence.split(";;") if cmd.strip()]
            self.macros[name] = commands
            print(f"[macro] ✅ Saved `{name}` with {len(commands)} commands.")

        elif subcmd == "run" and len(args) >= 2:
            name = args[1]
            if name not in self.macros:
                print(f"[macro] ❌ No macro named `{name}`.")
                return
            for raw in self.macros[name]:
                print(f"[macro →] {raw}")
                subcommand = parse_command(raw, context)
                run_command(subcommand, context)

        elif subcmd == "list":
            if not self.macros:
                print("[macro] (no macros saved)")
            for name, cmds in self.macros.items():
                print(f"• {name} ({len(cmds)} steps)")

        elif subcmd == "delete" and len(args) >= 2:
            name = args[1]
            if name in self.macros:
                del self.macros[name]
                print(f"[macro] 🗑️ Deleted `{name}`")
            else:
                print(f"[macro] ❌ No macro named `{name}`.")

        else:
            print("Usage: macro [save|run|list|delete]")

PLUGIN_REGISTRY = {
    "macro": MacroPlugin()
}
