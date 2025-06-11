class MemoryCore:
    def __init__(self):
        self.memory = {}

    def remember(self, key, value):
        """메모리에 데이터를 저장하는 메서드."""
        self.memory[key] = value
        return f"Stored: {key} -> {value}"

    def query(self, key):
        """메모리에서 특정 키의 값을 조회하는 메서드."""
        if key in self.memory:
            return f"{key}: {self.memory[key]}"
        return f"{key} not found"

    def delete(self, key):
        """메모리에서 특정 키-값 쌍을 삭제하는 메서드."""
        if key in self.memory:
            del self.memory[key]
            return f"Deleted {key}"
        return f"{key} not found"

    def reset(self):
        """메모리의 모든 데이터를 삭제하는 메서드."""
        self.memory.clear()
        return "Memory has been reset."

    def list_keys(self):
        """메모리에 저장된 모든 키를 리스트로 반환."""
        return list(self.memory.keys())

    def summarize(self):
        """메모리에 저장된 모든 데이터를 요약하여 반환."""
        if not self.memory:
            return "No memory stored."
        return "\n".join([f"{key}: {value}" for key, value in self.memory.items()])

    def get_all(self):
        """전체 메모리 데이터를 딕셔너리 형태로 반환."""
        return self.memory.copy()

