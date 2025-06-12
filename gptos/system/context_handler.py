from gptos.system.alias_manager import AliasManager

class SystemContext:
    def __init__(self):
        self.memory = []
        self.config = {
            "strict_mode": True
        }
        self.alias_manager = AliasManager()

    def log(self, command):
        from gptos.core.memory_core.recorder import record_command
        record_command(self, command)
