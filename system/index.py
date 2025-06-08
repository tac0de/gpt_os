# gpt_os/system/index.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.command_core import CommandCore
from core.memory_core import MemoryCore
from core.text_core import TextCore
from core.image_core import ImageCore
from core.philosophy_core import PhilosophyCore
from core.code_core import CodeCore

from system.state_manager import StateManager
from system.workflow_logger import WorkflowLogger
from interface.io_adapter import IOAdapter



class GPTOS:
    def __init__(self):
        self.state_manager = StateManager()
        self.workflow_logger = WorkflowLogger()
        self.io_adapter = IOAdapter()

        # 핵심 코어 모듈 초기화
        self.command_core = CommandCore(self.state_manager)
        self.memory_core = MemoryCore()
        self.text_core = TextCore()
        self.image_core = ImageCore()
        self.philosophy_core = PhilosophyCore()
        self.code_core = CodeCore()

        # Register all commands into the core
        from commands.register_all import register_all_commands
        register_all_commands(self.command_core, {
            "memory": self.memory_core,
            "text": self.text_core,
            "image": self.image_core,
            "philosophy": self.philosophy_core,
            "code": self.code_core
        })

        # 시스템 초기화 로그 기록
        self.workflow_logger.log("GPT OS Initialized")

    def run(self):
        self.workflow_logger.log("Starting GPT OS main loop")
        while True:
            user_input = self.io_adapter.read()
            if user_input in ["exit", "quit"]:
                self.workflow_logger.log("Exiting GPT OS")
                break
            response = self.command_core.execute(user_input)
            self.io_adapter.write(response)


def run_gpt_os():  # ✅ 외부 진입점
    os_instance = GPTOS()
    os_instance.run()

if __name__ == "__main__":
    run_gpt_os()
