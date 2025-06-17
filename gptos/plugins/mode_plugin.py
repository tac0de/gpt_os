from gptos.plugins.base import GPTOSPlugin

class ModePlugin(GPTOSPlugin):
    name = "mode"

    AVAILABLE_MODES = ["assistant", "editor", "critic"]

    def register(self, context):
        if "mode" not in context.config:
            context.config["mode"] = "assistant"

    def execute(self, command, context):
        args = command.args

        if not args:
            print(f"Current mode: {context.config.get('mode', 'assistant')}")
            return

        subcmd = args[0]

        if subcmd == "set" and len(args) >= 2:
            mode = args[1]
            if mode not in self.AVAILABLE_MODES:
                print(f"[mode] ❌ Invalid mode: {mode}")
                return
            context.config["mode"] = mode
            print(f"[mode] ✅ Changed to `{mode}`")

        elif subcmd == "list":
            print("Available modes:")
            for m in self.AVAILABLE_MODES:
                print(f"• {m}")

        else:
            print("Usage: mode [set <mode> | list]")

PLUGIN_REGISTRY = {
    "mode": ModePlugin()
}
