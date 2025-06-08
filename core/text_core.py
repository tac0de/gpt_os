# gpt_os/core/text_core.py

class TextCore:
    def __init__(self):
        # 향후 명령어 추론 패턴 등 확장 가능
        self.simple_aliases = {
            "시작해줘": "run",
            "적용해줘": "apply",
            "상태 보여줘": "report",
            "헬프": "help"
        }

    def alias_replace(self, input_text):
        """
        간단한 alias 기반의 명령어 변환
        예: "command_core 적용해줘" → "apply command_core"
        """
        for alias, true_cmd in self.simple_aliases.items():
            if alias in input_text:
                input_text = input_text.replace(alias, true_cmd)
        return input_text.strip()

    def parse(self, raw_input):
        normalized = self.alias_replace(raw_input)
        parts = normalized.strip().split()
        if not parts:
            return {"command": "", "args": []}
        return {"command": parts[0], "args": parts[1:]}

    def extract_command_keywords(self, input_text):
        """
        입력된 텍스트에서 의미 있는 명령어 토큰 추출
        예: "apply command_core please" → ("apply", ["command_core", "please"])
        """
        parts = input_text.strip().split()
        if not parts:
            return None, []
        return parts[0], parts[1:]
