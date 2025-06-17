# gptos/system/context_handler.py

from gptos.system.alias_manager import AliasManager
from gptos.system.command_log import logger

class SystemContext:
    def __init__(self):
        self.memory = []
        self.config = {
            "strict_mode": True,
            "log.level": "INFO",
            "memory.dedup": True,
            "summarize.recent_count": 10,
        }
        self.alias_manager = AliasManager()
        self.logger = logger  # Optional, in case access needed

    def log(
        self,
        command,
        *,
        parsed=None,
        result=None,
        error=None,
        status=None,
        duration=None,
        plugin=None,
    ):
        from gptos.core.memory_core.recorder import record_command
        record_command(self, command)

        self.logger.log(
            raw_input=command.raw,
            parsed=parsed,
            result=result,
            error=error,
            status=status,
            duration=duration,
            plugin=plugin,
        )
