from gptos.plugins.base import GPTOSPlugin
import random
import string

class GeneratePlugin(GPTOSPlugin):
    """Simple text and password generation."""
    name = "generate"

    def register(self, context):
        pass

    def execute(self, command, context):
        args = command.args
        if not args:
            self.print_usage()
            return

        sub = args[0]
        if sub == "password":
            length = int(args[1]) if len(args) > 1 else 12
            chars = string.ascii_letters + string.digits
            password = "".join(random.choice(chars) for _ in range(length))
            print(password)
        elif sub == "lorem":
            count = int(args[1]) if len(args) > 1 else 1
            words = [
                "lorem", "ipsum", "dolor", "sit", "amet", "consectetur",
                "adipiscing", "elit", "sed", "do", "eiusmod", "tempor"
            ]
            sentences = []
            for _ in range(count):
                n_words = random.randint(4, 10)
                sentence = " ".join(random.choice(words) for _ in range(n_words))
                sentences.append(sentence.capitalize() + ".")
            print(" ".join(sentences))
        else:
            self.print_usage()

    def print_usage(self):
        print("Usage: generate [password <len>|lorem <count>]")

PLUGIN_REGISTRY = {
    "generate": GeneratePlugin()
}
