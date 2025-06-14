from gptos.plugins.base import GPTOSPlugin
from gptos.codex.adapter import call_codex
from gptos.codex.tracker import PromptTracker

tracker = PromptTracker()

class CodexPlugin(GPTOSPlugin):
    name = "codex"

    def register(self, context): pass

    def execute(self, command, context):
        if not command.args:
            print("Usage: codex prompt <your prompt>")
            return

        sub = command.args[0]

        if sub == "prompt":
            user_prompt = " ".join(command.args[1:])
            tracker.record(user_prompt)
            print(f"[codex] Copy this into ChatGPT:\n{user_prompt}")
            return

        elif sub == "log":
            tracker.log()
            return
        elif sub == "save":
            name = command.args[1]
            path = f"gptos/plugins/{name}_plugin.py"
            with open(path, "w") as f:
                f.write(tracker.last_result or "# No result yet")
            print(f"[codex] Saved to {path}")

        print(f"[codex] Unknown subcommand: {sub}")


PLUGIN_REGISTRY = {
    "codex": CodexPlugin()
}