class TextCore:
    def __init__(self):
        self.log = []  # 로그 기록용 리스트
        self.theme = "light"
        self.loglevel = "info"

    def format_kv(self, key, value):
        return f"{key}: {value}"

    def format_output(self, type, text):
        return f"[{type}] {text}"

    # 로그 기록하는 함수
    def log_event(self, command, result):
        if callable(command):
            command = str(command)
        if callable(result):
            result = str(result)
        self.log.append({"command": command, "result": result})

    # 로그를 JSON 형식으로 내보내는 함수
    def export_log(self):
        import json
        return json.dumps(self.log, indent=4)

    # 로그를 출력하는 함수
    def log(self):
        return "\n".join([f"{entry['command']} -> {entry['result']}" for entry in self.log])

    # 로그를 파일로 저장하는 함수
    def save_log_to_file(self, filename="logfile.json"):
        import json
        with open(filename, "w") as f:
            json.dump(self.log, f, indent=4)
        return f"Log saved to {filename}"

