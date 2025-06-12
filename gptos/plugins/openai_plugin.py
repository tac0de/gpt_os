from gptos.plugins.base import GPTOSPlugin

# Placeholder import – requires `openai` package
# import openai

class AskPlugin(GPTOSPlugin):
    def register(self, context): pass

    def execute(self, command, context):
        if not command.args:
            print("Usage: ask <your question>")
            return

        query = " ".join(command.args)

        # Placeholder for API key
        # openai.api_key = "your-api-key-here"

        # Simulated output (replace with actual API call below)
        print("🤖 GPTOS is thinking about:", query)

        # Actual OpenAI call would be:
        # response = openai.ChatCompletion.create(
        #     model="gpt-4",
        #     messages=[{"role": "user", "content": query}]
        # )
        # print(response['choices'][0]['message']['content'])

PLUGIN_REGISTRY = {
    "ask": AskPlugin()
}
