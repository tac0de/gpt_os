from gptos.plugins.base import GPTOSPlugin
from gptos.core.philosophical_core.observer import ThoughtObserver
from gptos.core.philosophical_core.reasoner import reflect_on

class PhilosophyPlugin(GPTOSPlugin):
    def register(self, context):
        if not hasattr(context, "thoughts"):
            context.thoughts = ThoughtObserver()

    def execute(self, command, context):
        if not hasattr(context, "thoughts"):
            context.thoughts = ThoughtObserver()
        if command.name == "thoughts":
            thoughts = context.thoughts.list_thoughts()
            if not thoughts:
                print("🧘 No topics have been contemplated yet.")
            else:
                print("🧠 Topics contemplated:")
                for t in thoughts:
                    print(f" - {t}")
            return

        if not command.args:
            print("Usage: question <topic> or thoughts")
            return

        topic = " ".join(command.args)
        context.thoughts.log_topic(topic)
        print("🤔 " + reflect_on(topic))

PLUGIN_REGISTRY = {
    "question": PhilosophyPlugin(),
    "think": PhilosophyPlugin(),
    "thoughts": PhilosophyPlugin()  # now officially mapped
}
