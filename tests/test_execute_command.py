from io import StringIO
import sys
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from gptos.system.plugin_loader import load_plugins
from gptos.core.command_core import executor
from gptos.system.alias_manager import AliasManager

class DummyContext:
    def __init__(self):
        self.alias_manager = AliasManager()


def test_execute_hello_command():
    load_plugins()
    ctx = DummyContext()
    # Patch executor logger to avoid AttributeError
    class _DummyLogger:
        def info(self, *a, **k):
            pass
        def error(self, *a, **k):
            pass
        def log(self, *a, **k):
            pass

    executor.logger = _DummyLogger()

    # Make hello plugin execute asynchronously
    plugin = executor.PLUGIN_REGISTRY['hello']
    orig_execute = plugin.execute
    async def async_execute(command, context):
        return orig_execute(command, context)
    plugin.execute = async_execute

    buf = StringIO()
    with redirect_stdout(buf):
        executor.execute_command('hello', ctx)
    output = buf.getvalue()
    assert 'Hello, GPT OS!' in output

