# gptos/plugins/ethics_plugin.py

from gptos.plugins.base import GPTOSPlugin
from gptos.system.ethics import EthicsFilter, RiskLevel

class EthicsPlugin(GPTOSPlugin):
    name = "ethics"

    def register(self, context):
        pass  # Optional: future event hook registration

    def execute(self, command, context):
        if not command.args:
            print("Usage: evaluate ethics [your command]")
            return

        input_text = " ".join(command.args)
        filter = EthicsFilter()
        risk, reason = filter.evaluate(input_text)

        print(f"Risk: {risk.value.upper()} | Action: {'BLOCKED' if risk == RiskLevel.BLOCKED else 'ALLOWED'}")
        print(f"Reason: {reason}")

PLUGIN_REGISTRY = {
    "ethics": EthicsPlugin()
}

