from gptos.plugins.base import GPTOSPlugin
from gptos.system.command_log import logger
from gptos.core.memory_core.summarizer import summarize_memory  # 너가 작성한 함수

class SummarizerPlugin(GPTOSPlugin):
    name = "summarize"

    def register(self, context):
        pass

    def execute(self, command, context):
        args = command.args
        if not args or args[0] != "last":
            print("Usage: summarize last")
            return

        limit = int(args[1]) if len(args) > 1 and args[1].isdigit() else 10
        summary = summarize_memory(context, limit=limit)

        print(f"[Last {limit} command summaries]")
        print(summary)

PLUGIN_REGISTRY = {
    "summarize": SummarizerPlugin()
}
