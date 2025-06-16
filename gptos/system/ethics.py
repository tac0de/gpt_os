# gptos/system/ethics.py

from enum import Enum
from typing import List, Tuple, Callable
from functools import wraps

class RiskLevel(Enum):
    SAFE = "safe"
    WARNING = "warning"
    BLOCKED = "blocked"

class EthicsFilter:
    def __init__(self):
        self.blocklist = ["nuke", "kill", "suicide", "weaponize"]
        self.warnlist = ["hack", "exploit", "bypass", "inject"]

    def evaluate(self, text: str) -> Tuple[RiskLevel, str]:
        lowered = text.lower()
        for word in self.blocklist:
            if word in lowered:
                return (RiskLevel.BLOCKED, f"Detected blocked term: '{word}'")
        for word in self.warnlist:
            if word in lowered:
                return (RiskLevel.WARNING, f"Detected risky term: '{word}'")
        return (RiskLevel.SAFE, "No ethical issues detected.")

# ✅ 데코레이터 정의
def ethics_guard(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(command, context, *args, **kwargs):
        raw = command.raw if hasattr(command, "raw") else str(command)
        filter = EthicsFilter()
        risk, reason = filter.evaluate(raw)

        if risk == RiskLevel.BLOCKED:
            print(f"[ETHICS BLOCKED] Reason: {reason}")
            return f"Command blocked by ethics guard. ({reason})"

        if risk == RiskLevel.WARNING:
            print(f"[ETHICS WARNING] {reason}")

        return func(command, context, *args, **kwargs)
    return wrapper
