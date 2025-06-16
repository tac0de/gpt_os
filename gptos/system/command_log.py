import datetime
import json
import os
from typing import Optional, Any, Callable


class CommandLogEntry:
    def __init__(
        self,
        raw_input: str,
        parsed: Optional[dict] = None,
        result: Optional[Any] = None,
        error: Optional[Exception] = None
    ):
        self.timestamp: datetime.datetime = datetime.datetime.now()
        self.raw_input: str = raw_input
        self.parsed: Optional[dict] = parsed
        self.result: Optional[Any] = result
        self.error: Optional[Exception] = error

    def to_dict(self) -> dict:
        return {
            "timestamp": self.timestamp.isoformat(),
            "raw_input": self.raw_input,
            "parsed": self.parsed,
            "result": str(self.result)[:200],
            "error": str(self.error) if self.error else None,
        }

    def __repr__(self):
        return f"<CommandLogEntry {self.timestamp} '{self.raw_input}'>"


class CommandLogger:
    def __init__(self):
        self.entries: list[CommandLogEntry] = []

    def log(
        self,
        raw_input: str,
        parsed: Optional[dict] = None,
        result: Optional[Any] = None,
        error: Optional[Exception] = None
    ):
        entry = CommandLogEntry(raw_input, parsed, result, error)
        self.entries.append(entry)

    def latest(self) -> Optional[CommandLogEntry]:
        return self.entries[-1] if self.entries else None

    def get_recent(self, limit: int = 10) -> list[CommandLogEntry]:
        return self.entries[-limit:]

    def search(self, keyword: str) -> list[CommandLogEntry]:
        kw = keyword.lower()
        return [
            entry for entry in self.entries
            if kw in entry.raw_input.lower()
            or kw in str(entry.result).lower()
            or (entry.parsed and kw in str(entry.parsed).lower())
        ]

    def filter_errors(self) -> list[CommandLogEntry]:
        return [entry for entry in self.entries if entry.error]

    def filter_by_time(self, delta_minutes: int = 30) -> list[CommandLogEntry]:
        now = datetime.datetime.now()
        threshold = now - datetime.timedelta(minutes=delta_minutes)
        return [entry for entry in self.entries if entry.timestamp >= threshold]

    def replay(self, index: int, executor_fn: Callable[[str, dict], Any], context: dict):
        if 0 <= index < len(self.entries):
            raw_input = self.entries[index].raw_input
            print(f"[REPLAY] #{index}: {raw_input}")
            return executor_fn(raw_input, context)
        print(f"[REPLAY] Invalid index: {index}")

    def replay_last(self, executor_fn: Callable[[str, dict], Any], context: dict):
        if not self.entries:
            print("[REPLAY] No commands available.")
            return
        return self.replay(len(self.entries) - 1, executor_fn, context)

    def export(self) -> list[dict]:
        return [entry.to_dict() for entry in self.entries]

    def save_to_file(self, filepath: str):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.export(), f, indent=2)
        print(f"[LOG] Saved to {filepath}")

    def load_from_file(self, filepath: str):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.entries = [
                    CommandLogEntry(
                        raw_input=e["raw_input"],
                        parsed=e.get("parsed"),
                        result=e.get("result"),
                        error=e.get("error")
                    )
                    for e in data
                ]
            print(f"[LOG] Loaded from {filepath}")
        except FileNotFoundError:
            print(f"[LOG] File not found: {filepath}")
        except Exception as e:
            print(f"[LOG] Failed to load: {e}")

    def clear(self):
        self.entries.clear()

# Singleton instance
logger = CommandLogger()
