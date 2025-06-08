import unittest
from core.command_core import CommandCore

class DummyCore:
    def remember(self, args):
        return f"REMEMBER: {' '.join(args)}"
    def recall(self, args):
        return f"RECALL: {' '.join(args)}"
    def forget(self, args):
        return f"FORGET: {' '.join(args)}"

class DummyIO:
    def __init__(self):
        self.outputs = []
    def write(self, message):
        self.outputs.append(message)

class DummyLogger:
    def log(self, command, args):
        pass

class TestCommandCore(unittest.TestCase):
    def setUp(self):
        self.command_core = CommandCore()
        self.command_core.register_core("memory", DummyCore())
        self.command_core.io = DummyIO()
        self.command_core.logger = DummyLogger()

        # Register dummy commands
        self.command_core.register_command("remember", self.command_core.cores["memory"].remember, description="store memory")
        self.command_core.register_command("recall", self.command_core.cores["memory"].recall, description="get memory")
        self.command_core.register_command("forget", self.command_core.cores["memory"].forget, description="remove memory")

    def test_remember_command(self):
        self.command_core.execute("remember", ["goal", "success"])
        self.assertIn("REMEMBER: goal success", self.command_core.io.outputs[-1])

    def test_recall_command(self):
        self.command_core.execute("recall", ["goal"])
        self.assertIn("RECALL: goal", self.command_core.io.outputs[-1])

    def test_unknown_command(self):
        self.command_core.execute("undefined", ["something"])
        self.assertIn("Unknown command: undefined", self.command_core.io.outputs[-1])

if __name__ == '__main__':
    unittest.main()