from gptos.plugins.base import GPTOSPlugin
import sys

class DevtoolsPlugin(GPTOSPlugin):
    def register(self, context): pass

    def execute(self, command, context):
        if not command.args:
            print("Usage: dev [echo|simulate|plugins|context]")
            return

        sub = command.args[0]

        if sub == "echo":
            msg = " ".join(command.args[1:])
            print(f"[echo] {msg}")
            return

        if sub == "simulate":
            try:
                n = int(command.args[1])
                for i in range(n):
                    fake_cmd = type("FakeCommand", (), {"name": f"fake{i}", "args": []})()
                    context.memory.append(fake_cmd)
                print(f"[simulate] Added {n} fake memory entries.")
            except:
                print("Usage: dev simulate <number>")
            return

        if sub == "plugins":
            # ✅ FIX: fetch live registry at runtime
            plugin_loader = sys.modules.get("gptos.system.plugin_loader")
            registry = plugin_loader.PLUGIN_REGISTRY if plugin_loader else {}
            print("[plugins] Loaded:")
            for name in sorted(registry.keys()):
                print(f" - {name}")
            return

        if sub == "context":
            print("[context] Memory length:", len(context.memory))
            print("[context] Config:", context.config)
            return

        print(f"[dev] Unknown subcommand: {sub}")

PLUGIN_REGISTRY = {
    "dev": DevtoolsPlugin()
}
