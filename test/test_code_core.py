import unittest
from core.code_core import CodeCore

class TestCodeCore(unittest.TestCase):
    def setUp(self):
        self.code_core = CodeCore()

    def test_evaluate_valid_expression(self):
        result = self.code_core.evaluate(["2", "+", "3"])
        self.assertEqual(result, "5")

    def test_evaluate_invalid_expression(self):
        result = self.code_core.evaluate(["2", "+", "unknown_var"])
        self.assertTrue("Error" in result or "invalid" in result.lower())

    def test_execute_print_statement(self):
        result = self.code_core.execute("print('Hello')")
        self.assertIn("🖨️ Output", result)
        self.assertIn("Hello", result)

    def test_execute_error_code(self):
        result = self.code_core.execute("raise Exception('fail')")
        self.assertTrue(result.startswith("❌ Execution error"))

if __name__ == '__main__':
    unittest.main()
