# core/text_core.py

from datetime import datetime
import json

class TextCore:
    """
    Handles output formatting and basic session logging.
    """

    def __init__(self):
        self.log_history = []

    def format_output(self, label: str, content: str) -> str:
        return f"[{label.upper()}]\n{content}"

    def format_kv(self, key: str, value: str) -> str:
        return f"{key} → {value}"

    def log_event(self, command: str, result: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{timestamp} | {command} => {result}"
        self.log_history.append(entry)

    def print_log(self):
        print("[SESSION LOG]")
        for entry in self.log_history:
            print(" ", entry)

    def clear_log(self):
        self.log_history.clear()
    
    def export_log(self) -> str:
        structured_logs = []
        for entry in self.log_history:
            try:
                parts = entry.split(" | ", 1)
                timestamp = parts[0]
                rest = parts[1].split(" => ")
                command = rest[0]
                output = rest[1] if len(rest) > 1 else ""
                structured_logs.append({
                    "timestamp": timestamp,
                    "command": command,
                    "output": output
                })
            except Exception:
                continue  # skip malformed entries
        return json.dumps(structured_logs, indent=2)
    def save_log_to_file(self, filename: str = "logs.json") -> str:
        try:
            json_data = self.export_log()
            with open(filename, "w", encoding="utf-8") as f:
                f.write(json_data)
            return f"Log successfully saved to {filename}"
        except Exception as e:
            return f"Failed to save log: {str(e)}"

