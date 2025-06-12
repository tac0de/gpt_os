from gptos.plugins.base import GPTOSPlugin

class AliasPlugin(GPTOSPlugin):
    def register(self, context): pass

    def execute(self, command, context):
        if not command.args:
            print("Usage:")
            print(" - alias foo=bar     (create alias)")
            print(" - alias             (list aliases)")
            return

        for arg in command.args:
            if "=" in arg:
                alias, target = arg.split("=", 1)
                context.alias_manager.define(alias, target)
                print(f"Alias defined: {alias} → {target}")
            else:
                print("Invalid format. Use: alias foo=bar")

PLUGIN_REGISTRY = {
    "alias": AliasPlugin()
}
