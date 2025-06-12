from gptos.plugins.base import GPTOSPlugin
from gptos.core.memory_core.summarizer import summarize_memory

class MemoryPlugin(GPTOSPlugin):
    def register(self, context): pass

    def execute(self, command, context):
        output = summarize_memory(context)
        print("🧠 Recent Commands:\n" + output)

PLUGIN_REGISTRY = {
    "memory": MemoryPlugin()
}
