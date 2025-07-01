# gptos/plugins/log_plugin.py

from gptos.plugins.base import GPTOSPlugin
from gptos.system.command_log import command_logger, CommandLogEntry

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
            entries = command_logger.entries[-limit:]
            self.print_entries(entries)

        elif subcommand == "search" and len(args) > 1:
            keyword = " ".join(args[1:])
            results = [e for e in command_logger.entries if keyword.lower() in e.raw_input.lower()]
            self.print_entries(results)

        elif subcommand == "filter" and "--error" in args:
            errors = [e for e in command_logger.entries if e.error]
            self.print_entries(errors)

        elif subcommand == "save" and len(args) > 1:
            command_logger.save_to_file(args[1])

        elif subcommand == "load" and len(args) > 1:
            command_logger.load_from_file(args[1])

        elif subcommand == "replay" and len(args) > 1 and args[1].isdigit():
            index = int(args[1])
            command_logger.replay(index, context["executor"], context)

        elif subcommand == "replay" and len(args) > 1 and args[1] == "last":
            command_logger.replay_last(context["executor"], context)
        elif subcommand == "filter":
            filters = self.parse_filters(args[1:])
            results = self.filter_entries(command_logger.entries, filters)
            self.print_entries(results)
        else:
            print("Invalid log command. Try: log recent | log search <kw> | log filter --error | log save path | log replay 2")

    def parse_filters(self, args):
        filters = {}
        i = 0
        while i < len(args):
            if args[i] == "--plugin" and i+1 < len(args):
                filters["plugin"] = args[i+1]
                i += 2
            elif args[i] == "--status" and i+1 < len(args):
                filters["status"] = args[i+1].upper()
                i += 2
            elif args[i] == "--min-duration" and i+1 < len(args):
                filters["min_duration"] = float(args[i+1])
                i += 2
            elif args[i] == "--max-duration" and i+1 < len(args):
                filters["max_duration"] = float(args[i+1])
                i += 2
            else:
                i += 1
        return filters

    def filter_entries(self, entries: list[CommandLogEntry], filters: dict):
        result = entries
        if "plugin" in filters:
            result = [e for e in result if e.plugin == filters["plugin"]]
        if "status" in filters:
            result = [e for e in result if e.status == filters["status"]]
        if "min_duration" in filters:
            result = [e for e in result if e.duration and e.duration >= filters["min_duration"]]
        if "max_duration" in filters:
            result = [e for e in result if e.duration and e.duration <= filters["max_duration"]]
        return result

    def print_entries(self, entries: list[CommandLogEntry]):
        if not entries:
            print("[log] No matching entries.")
            return
        for i, entry in enumerate(entries):
            ts = entry.timestamp.strftime("%H:%M:%S")
            dur = f"{entry.duration:.2f}s" if entry.duration else "-"
            status_icon = "❌" if entry.status == "ERROR" else "✅"
            print(f"{i:02d} [{ts}] {status_icon} ({entry.plugin}) {entry.raw_input} ⏱ {dur}")

PLUGIN_REGISTRY = {
    "log": LogPlugin()
}
