import unittest
import os
import json
from gptos.system.os_manager import OSManager

class TestConfigLoader(unittest.TestCase):
    def setUp(self):
        self.test_config_path = ".gptosrc"
        self.test_config = {
            "alias": {"m": "mem"},
            "startup_memory": {"foo": "bar"},
            "autocommands": ["remember alpha beta"]
        }
        with open(self.test_config_path, "w") as f:
            json.dump(self.test_config, f)

        self.os = OSManager()

    def tearDown(self):
        if os.path.exists(self.test_config_path):
            os.remove(self.test_config_path)

    def test_alias_applied(self):
        self.assertEqual(self.os.alias.resolve("m"), "mem")

    def test_startup_memory_loaded(self):
        self.assertIn("foo", self.os.memory.memory)
        self.assertEqual(self.os.memory.memory["foo"], "bar")

    def test_autocommand_executed(self):
        self.assertIn("alpha", self.os.memory.memory)
        self.assertEqual(self.os.memory.memory["alpha"], "beta")
