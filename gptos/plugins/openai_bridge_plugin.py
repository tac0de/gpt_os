from gptos.plugins.base import GPTOSPlugin
import openai
import os
from gptos.system.api_config import get_api_key

class OpenAIBridgePlugin(GPTOSPlugin):
    name = "openai"

    def register(self, context):
        api_key = get_api_key(context.config, "openai.api_key", "OPENAI_API_KEY")

        if not api_key:
            print("[openai] ❌ No API key configured. Set with: config set openai.api_key <key>")
        else:
            openai.api_key = api_key

    def execute(self, command, context):
        if not command.args:
            print("Usage: openai ask <prompt>")
            return

        subcmd = command.args[0]

        if subcmd == "ask":
            prompt = " ".join(command.args[1:])
            if not prompt:
                print("[openai] Empty prompt.")
                return

            print(f"[openai] 🔍 Asking: {prompt}")
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a command assistant."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7
                )
                answer = response.choices[0].message.content.strip()
                print(f"[openai] ✅ Response:\n{answer}")
            except Exception as e:
                print(f"[openai] ❌ Error: {e}")
        else:
            print("Usage: openai ask <prompt>")

PLUGIN_REGISTRY = {
    "openai": OpenAIBridgePlugin()
}
