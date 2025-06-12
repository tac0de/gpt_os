from abc import ABC, abstractmethod

class GPTOSPlugin(ABC):
    @abstractmethod
    def register(self, context): pass

    @abstractmethod
    def execute(self, command, context): pass
