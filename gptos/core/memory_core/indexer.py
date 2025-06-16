from typing import List, Dict

class MemoryIndexer:
    def __init__(self):
        self.index: Dict[str, List[str]] = {}

    def add_entry(self, category: str, content: str) -> None:
        if category not in self.index:
            self.index[category] = []
        self.index[category].append(content)

    def get_entries(self, category: str) -> List[str]:
        return self.index.get(category, [])

    def get_all_categories(self) -> List[str]:
        return list(self.index.keys())