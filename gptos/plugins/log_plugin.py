from gptos.plugins.base import GPTOSPlugin
from gptos.system.command_log import logger

DEFAULT_LOG_PATH = ".gptos/command_log.json"

class LogPlugin(GPTOSPlugin):
    name = "log"

    def register(self, context): pass

    def execute(self, command, context):
        if not command.args:
            print("Usage: log [save|load|clear|show]")
            return

        sub = command.args[0]

        if sub == "save":
            path = command.args[1] if len(command.args) > 1 else DEFAULT_LOG_PATH
            logger.save_to_file(path)

        elif sub == "load":
            path = command.args[1] if len(command.args) > 1 else DEFAULT_LOG_PATH
            logger.load_from_file(path)

        elif sub == "clear":
            confirm = input("⚠️ Confirm clear all logs? (y/n): ")
            if confirm.lower() == "y":
                logger.clear()
                print("[log] Cleared.")
            else:
                print("[log] Cancelled.")

        elif sub == "show":
            for i, entry in enumerate(logger.entries):
                print(f"[{i}] {entry.raw_input}")

        else:
            print(f"[log] Unknown subcommand: {sub}")

PLUGIN_REGISTRY = {
    "log": LogPlugin()
}
