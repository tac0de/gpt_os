# gptos/codex/adapter.py
def call_codex(prompt, temperature=0.2, max_tokens=400):
    print("[codex] Simulated mode: copy the prompt into ChatGPT")
    print("------")
    print(prompt)
    print("------")
    return "# (Paste the response here into your plugin manually)"
