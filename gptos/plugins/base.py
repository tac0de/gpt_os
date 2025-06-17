# gptos/system/plugins/base.py
from abc import ABC, abstractmethod

class GPTOSPlugin(ABC):
    @abstractmethod
    def register(self, context):
        """Registers the plugin with the provided context."""
        pass

    @abstractmethod
    def execute(self, command, context):
        """Execute the plugin with the given command and context."""
        pass
