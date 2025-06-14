from gptos.plugins.base import GPTOSPlugin
import sys
from gptos.system.command_log import logger  # 🔁 use shared instance
from gptos.system.executor_wrapper import executor_fn

class DevtoolsPlugin(GPTOSPlugin):
    def register(self, context): pass

    def execute(self, command, context):
        if not command.args:
            print("Usage: dev [echo|simulate|plugins|context|replay|log]")
            return

        sub = command.args[0]

        if sub == "echo":
            msg = " ".join(command.args[1:])
            print(f"[echo] {msg}")
            return

        elif sub == "simulate":
            try:
                n = int(command.args[1])
                for i in range(n):
                    fake_cmd = type("FakeCommand", (), {"name": f"fake{i}", "args": []})()
                    context.memory.append(fake_cmd)
                print(f"[simulate] Added {n} fake memory entries.")
            except Exception:
                print("Usage: dev simulate <number>")
            return

        elif sub == "plugins":
            plugin_loader = sys.modules.get("gptos.system.plugin_loader")
            registry = plugin_loader.PLUGIN_REGISTRY if plugin_loader else {}
            print("[plugins] Loaded:")
            for name in sorted(registry.keys()):
                print(f" - {name}")
            return

        elif sub == "context":
            print("[context] Memory length:", len(context.memory))
            print("[context] Config:", context.config)
            return

        elif sub == "replay":
            if len(command.args) < 2:
                print("Usage: dev replay <index|last|-1>")
                return

            target = command.args[1]

            if target == "last" or target == "-1":
                logger.replay_last(executor_fn, context)
            else:
                try:
                    index = int(target)
                    logger.replay(index, executor_fn, context)
                except ValueError:
                    print("Usage: dev replay <index|last|-1>")
            return

        elif sub == "log":
            if not logger.entries:
                print("[log] No entries yet.")
            else:
                for i, entry in enumerate(logger.entries):
                    print(f"[{i}] {entry.raw_input}")
            return

        # ❗️ Only here if no match
        print(f"[dev] Unknown subcommand: {sub}")


PLUGIN_REGISTRY = {
    "dev": DevtoolsPlugin()
}
