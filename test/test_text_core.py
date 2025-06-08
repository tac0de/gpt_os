import unittest
from core.text_core import TextCore

class TestTextCore(unittest.TestCase):
    def setUp(self):
        self.parser = TextCore()

    def test_simple_command(self):
        parsed = self.parser.parse("remember goal become architect")
        self.assertEqual(parsed["command"], "remember")
        self.assertEqual(parsed["args"], ["goal", "become", "architect"])

    def test_empty_input(self):
        parsed = self.parser.parse("")
        self.assertEqual(parsed["command"], "")
        self.assertEqual(parsed["args"], [])

    def test_whitespace_input(self):
        parsed = self.parser.parse("   ")
        self.assertEqual(parsed["command"], "")
        self.assertEqual(parsed["args"], [])

    def test_single_word(self):
        parsed = self.parser.parse("help")
        self.assertEqual(parsed["command"], "help")
        self.assertEqual(parsed["args"], [])

if __name__ == '__main__':
    unittest.main()
