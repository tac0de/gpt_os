from gptos.plugins.base import GPTOSPlugin

class HelloPlugin(GPTOSPlugin):
    def register(self, context): pass

    def execute(self, command, context):
        print("Hello, GPT OS!")

PLUGIN_REGISTRY = {
    "hello": HelloPlugin()
}
