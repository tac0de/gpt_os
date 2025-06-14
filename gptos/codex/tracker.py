class PromptTracker:
    def __init__(self):
        self.prompts = []
        self.last_prompt = None
        self.last_result = None

    def record(self, prompt, result="(pending)"):
        entry = {"prompt": prompt, "result": result}
        self.prompts.append(entry)
        self.last_prompt = prompt
        self.last_result = result

    def log(self):
        for i, entry in enumerate(self.prompts):
            print(f"[{i}] {entry['prompt']}")
