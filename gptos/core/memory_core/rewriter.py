from typing import List

class MemoryRewriter:
    def __init__(self, context):
        self.context = context
    def deduplicate(self, entries: List[str]) -> List[str]:
        seen = set()
        result = []
        for entry in entries:
            if entry not in seen:
                seen.add(entry)
                result.append(entry)
        return result

    def rewrite_summary(self, entries: List[str]) -> str:
        return " / ".join(entry.strip() for entry in entries[:3]) + " ..."
