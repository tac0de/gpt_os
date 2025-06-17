from gptos.plugins.base import GPTOSPlugin

class ConfigPlugin(GPTOSPlugin):
    def register(self, context):
        # Optional: 초기값 강제 삽입 가능
        context.config.setdefault("log.level", "INFO")
        context.config.setdefault("memory.dedup", True)
        context.config.setdefault("summarize.recent_count", 10)

    def execute(self, command, context):
        if not command.args:
            print("Usage: config [key] [value]")
            return

        key = command.args[0]
        if len(command.args) == 1:
            value = context.config.get(key, "<not set>")
            print(f"{key} = {value}")
        else:
            raw_value = command.args[1]
            parsed_value = parse_value(raw_value)
            context.config[key] = parsed_value
            print(f"{key} set to {parsed_value}")

def parse_value(val):
    if val.lower() in ("true", "on", "yes"):
        return True
    elif val.lower() in ("false", "off", "no"):
        return False
    try:
        return int(val)
    except ValueError:
        return val

PLUGIN_REGISTRY = {
    "config": ConfigPlugin()
}
