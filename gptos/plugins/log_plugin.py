# gptos/plugins/log_plugin.py

from gptos.plugins.base import GPTOSPlugin
from gptos.system.command_log import logger, CommandLogEntry

class LogPlugin(GPTOSPlugin):
    name = "log"

    def register(self, context):
        pass

    def execute(self, command, context):
        args = command.args
        if not args:
            print("Usage: log [recent|search <keyword>|filter --error|save <path>|load <path>|replay <index>|replay last]")
            return

        subcommand = args[0]

        if subcommand == "recent":
            limit = int(args[1]) if len(args) > 1 and args[1].isdigit() else 10
            entries = logger.entries[-limit:]
            self.print_entries(entries)

        elif subcommand == "search" and len(args) > 1:
            keyword = " ".join(args[1:])
            results = [e for e in logger.entries if keyword.lower() in e.raw_input.lower()]
            self.print_entries(results)

        elif subcommand == "filter" and "--error" in args:
            errors = [e for e in logger.entries if e.error]
            self.print_entries(errors)

        elif subcommand == "save" and len(args) > 1:
            logger.save_to_file(args[1])

        elif subcommand == "load" and len(args) > 1:
            logger.load_from_file(args[1])

        elif subcommand == "replay" and len(args) > 1 and args[1].isdigit():
            index = int(args[1])
            logger.replay(index, context["executor"], context)

        elif subcommand == "replay" and len(args) > 1 and args[1] == "last":
            logger.replay_last(context["executor"], context)

        else:
            print("Invalid log command. Try: log recent | log search <kw> | log filter --error | log save path | log replay 2")

    def print_entries(self, entries: list[CommandLogEntry]):
        if not entries:
            print("[log] No matching entries.")
            return
        for i, entry in enumerate(entries):
            ts = entry.timestamp.strftime("%H:%M:%S")
            raw = entry.raw_input
            if entry.error:
                print(f"{i:02d} [{ts}] ❌ {raw} → {entry.error}")
            else:
                print(f"{i:02d} [{ts}] ✅ {raw}")

PLUGIN_REGISTRY = {
    "log": LogPlugin()
}
