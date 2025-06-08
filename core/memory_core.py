# gpt_os/core/memory_core.py
import json
import os

class MemoryCore:
    def __init__(self, storage_path="core/memory.json"):
        self.memory_slots = {}
        self.storage_path = storage_path
        self.load()

    def remember(self, key, value):
        """
        Store a value under a specific key in memory.
        """
        self.memory_slots[key] = value
        self.save()
        return f"Memory stored: [{key}] → {value}"

    def recall(self, key):
        """
        Retrieve a value stored under a key.
        """
        return self.memory_slots.get(key, f"No memory found for '{key}'.")

    def forget(self, key):
        """
        Delete a specific memory slot.
        """
        if key in self.memory_slots:
            del self.memory_slots[key]
            self.save()
            return f"Memory for '{key}' has been deleted."
        return f"No memory found for '{key}'."

    def list_memory(self):
        """
        List all current memory entries.
        """
        if not self.memory_slots:
            return "No memories stored."
        return "\n".join([f"- {k}: {v}" for k, v in self.memory_slots.items()])
    def save(self):
        try:
            with open(self.storage_path, "w", encoding="utf-8") as f:
                json.dump(self.memory, f, indent=2)
        except Exception as e:
            return f"Error saving memory: {e}"
    def load(self):
        if os.path.exists(self.storage_path):
            try:
                with open(self.storage_path, "r", encoding="utf-8") as f:
                    self.memory = json.load(f)
            except Exception:
                self.memory = {}


