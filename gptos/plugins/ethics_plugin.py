from gptos.plugins.base import GPTOSPlugin

SUSPICIOUS_KEYWORDS = [
    "force", "bypass", "delete", "hack", "shutdown", "root", "violate", "fake"
]

class EthicsPlugin(GPTOSPlugin):
    def register(self, context): pass

    def execute(self, command, context):
        memory = context.memory
        flagged = []

        for cmd in memory:
            cmd_line = f"{cmd.name} {' '.join(cmd.args)}".lower()
            if any(keyword in cmd_line for keyword in SUSPICIOUS_KEYWORDS):
                flagged.append(cmd_line)

        if not flagged:
            print("✅ Ethics Report: No violations detected.")
        else:
            print(f"⚠️ Ethics Report: {len(flagged)} suspicious commands found:")
            for line in flagged:
                print(f" - {line}")

PLUGIN_REGISTRY = {
    "ethics": EthicsPlugin()
}
