import unittest
from gptos.system.alias_manager import AliasManager

class TestAliasManager(unittest.TestCase):
    def setUp(self):
        self.alias = AliasManager()
        config = {
            "alias": {
                "ls": "list",
                "rm": "delete",
                "mem": "summarize"
            }
        }
        self.alias.load_from_dict(config)

    def test_resolve_alias(self):
        self.assertEqual(self.alias.resolve("ls"), "list")
        self.assertEqual(self.alias.resolve("rm alpha"), "delete alpha")
        self.assertEqual(self.alias.resolve("mem"), "summarize")

    def test_resolve_non_alias(self):
        self.assertEqual(self.alias.resolve("remember foo bar"), "remember foo bar")
