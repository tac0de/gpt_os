# gptos/system/alias_manager.py

class AliasManager:
    def __init__(self):
        self.aliases = {}

    def set_alias(self, name: str, value: str):
        self.aliases[name] = value

    def get(self, name: str) -> str:
        return self.aliases.get(name, "")

    def get_all(self) -> dict:
        return self.aliases.copy()

    def resolve(self, name: str) -> str:
        """Returns alias value or original if not defined."""
        return self.aliases.get(name, name)
