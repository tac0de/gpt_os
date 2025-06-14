import datetime
from typing import Optional, Any
import json
import os

class CommandLogEntry:
    def __init__(self, raw_input: str, parsed: Optional[dict] = None,
                 result: Optional[Any] = None, error: Optional[Exception] = None):
        self.timestamp = datetime.datetime.now()
        self.raw_input = raw_input
        self.parsed = parsed
        self.result = result
        self.error = error

    def to_dict(self) -> dict:
        return {
            "timestamp": self.timestamp.isoformat(),
            "raw_input": self.raw_input,
            "parsed": self.parsed,
            "result": str(self.result)[:200],  # Truncate long output
            "error": str(self.error) if self.error else None,
        }

    def __repr__(self):
        return f"<CommandLogEntry {self.timestamp} '{self.raw_input}'>"

class CommandLogger:
    def __init__(self):
        self.entries: list[CommandLogEntry] = []

    def log(self, raw_input: str, parsed: Optional[dict] = None,
            result: Optional[Any] = None, error: Optional[Exception] = None):
        entry = CommandLogEntry(raw_input, parsed, result, error)
        self.entries.append(entry)

    def latest(self) -> Optional[CommandLogEntry]:
        return self.entries[-1] if self.entries else None

    def export(self) -> list[dict]:
        return [entry.to_dict() for entry in self.entries]

    def clear(self):
        self.entries.clear()
    
    def replay(self, index: int, executor_fn, context):
        """Replay a command by index using provided executor function."""
        if 0 <= index < len(self.entries):
            raw_input = self.entries[index].raw_input
            print(f"[REPLAY] #{index}: {raw_input}")
            return executor_fn(raw_input, context)
        else:
            print(f"Invalid log index: {index}")

    def save_to_file(self, filepath: str):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.export(), f, indent=2)
        print(f"[log] Saved to {filepath}")

    def load_from_file(self, filepath: str):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.entries = [
                    CommandLogEntry(
                        raw_input=entry['raw_input'],
                        parsed=entry.get('parsed'),
                        result=entry.get('result'),
                        error=entry.get('error')
                    ) for entry in data
                ]
            print(f"[log] Loaded from {filepath}")
        except FileNotFoundError:
            print(f"[log] File not found: {filepath}")
        except Exception as e:
            print(f"[log] Failed to load: {e}")
    def replay_last(self, executor_fn, context):
        if not self.entries:
            print("[replay] No previous command to replay.")
            return
        return self.replay(len(self.entries) - 1, executor_fn, context)


# Shared singleton instance
logger = CommandLogger()
