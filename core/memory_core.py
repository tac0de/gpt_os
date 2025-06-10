# core/memory_core.py

class MemoryCore:
    """
    Stores and retrieves memory in a simple key-value store.
    """
    def __init__(self):
        self.memory = {}

    def remember(self, key: str, value: str):
        self.memory[key] = value

    def query(self, key: str) -> str:
        return self.memory.get(key, "[NOT FOUND]")

    def reset(self):
        self.memory.clear()
        print("[MEMORY] Memory reset")

    def get_all(self) -> dict:
        return self.memory.copy()
    
    def delete(self, key: str) -> bool:
        if key in self.memory:
            del self.memory[key]
            return True
        return False
    def list_keys(self) -> list:
        return list(self.memory.keys())
    
    def summarize(self) -> str:
        if not self.memory:
            return "No memory stored."
        return "\n".join(f"{key} → {value}" for key, value in self.memory.items())



