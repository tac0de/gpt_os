# system/alias_manager.py
class AliasManager:
    def __init__(self, alias_map=None):
        self.alias_map = alias_map or {}

    def load_from_dict(self, config_dict):
        self.alias_map.update(config_dict.get("alias", {}))

    def resolve(self, command_str):
        parts = command_str.strip().split()
        if parts and parts[0] in self.alias_map:
            parts[0] = self.alias_map[parts[0]]
        return " ".join(parts)
