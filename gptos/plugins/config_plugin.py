from gptos.plugins.base import GPTOSPlugin

class ConfigPlugin(GPTOSPlugin):
    def register(self, context): pass

    def execute(self, command, context):
        if not command.args:
            print("Usage: config [key] [value]")
            return

        key = command.args[0]
        if len(command.args) == 1:
            # Get config value
            value = context.config.get(key, "<not set>")
            print(f"{key} = {value}")
        else:
            # Set config value
            value = command.args[1]
            parsed_value = parse_value(value)
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
