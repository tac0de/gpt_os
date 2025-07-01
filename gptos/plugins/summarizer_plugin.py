from gptos.plugins.base import GPTOSPlugin
from gptos.system.command_log import command_logger, CommandLogEntry
from collections import defaultdict

class SummarizePlugin(GPTOSPlugin):
    name = "summarize"

    def register(self, context):
        pass

    def execute(self, command, context):
        args = command.args
        if not args:
            print("Usage: summarize [usage]")
            return

        subcommand = args[0]
        if subcommand == "usage":
            self.summarize_plugin_usage(command_logger.entries)

    def summarize_plugin_usage(self, entries: list[CommandLogEntry]):
        stats = defaultdict(lambda: {
            "count": 0,
            "errors": 0,
            "total_duration": 0.0
        })

        for entry in entries:
            plugin = entry.plugin or "unknown"
            stats[plugin]["count"] += 1
            if entry.error:
                stats[plugin]["errors"] += 1
            if entry.duration:
                stats[plugin]["total_duration"] += entry.duration

        # 정렬: 사용 횟수 내림차순
        sorted_stats = sorted(stats.items(), key=lambda item: item[1]["count"], reverse=True)

        print("Summary of plugin usage:")
        print("────────────────────────────")
        for plugin, data in sorted_stats:
            count = data["count"]
            errors = data["errors"]
            avg_duration = data["total_duration"] / count if count > 0 else 0.0
            bar = "▍" * min(count, 10)
            print(f"{plugin:<10} {bar:<10} {count:>3} cmds, {errors:>2} errors, avg {avg_duration:.2f}s")

PLUGIN_REGISTRY = {
    "summarize": SummarizePlugin()
}
