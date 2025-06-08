# gpt_os/core/code_core.py

import io
import contextlib

class CodeCore:
    def __init__(self):
        self.snippet_history = []

    def evaluate(self, code_string):
        """
        Evaluate a Python expression or snippet safely (no imports or side-effects).
        """
        try:
            result = eval(code_string, {"__builtins__": {}})
            return f"✅ Result: {result}"
        except Exception as e:
            return f"❌ Error: {e}"

    def execute(self, code_string):
        """
        Execute a code block and capture stdout output.
        """
        self.snippet_history.append(code_string)
        buffer = io.StringIO()
        try:
            with contextlib.redirect_stdout(buffer):
                exec(code_string, {"__builtins__": {}})
            output = buffer.getvalue()
            return f"🖨️ Output:\n{output or '(no output)'}"
        except Exception as e:
            return f"❌ Execution error: {e}"

    def history(self, limit=5):
        return self.snippet_history[-limit:]
