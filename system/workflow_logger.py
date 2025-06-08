# gpt_os/system/workflow_logger.py
from datetime import datetime

class WorkflowLogger:
    def __init__(self):
        self.logs = []

    def log(self, message):
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        entry = f"{timestamp} {message}"
        self.logs.append(entry)
        print(entry)  # 실시간 출력용

    def last(self, n=5):
        return "\n".join(self.logs[-n:])

    def all(self):
        return "\n".join(self.logs)

    def clear(self):
        self.logs = []
        return "Workflow logs cleared."
