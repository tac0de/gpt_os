import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from gptos.core.command_core.parser import parse_command, Command
from gptos.system.alias_manager import AliasManager

class DummyContext:
    def __init__(self):
        self.alias_manager = AliasManager()


def test_parse_basic():
    cmd = parse_command('foo bar baz')
    assert isinstance(cmd, Command)
    assert cmd.name == 'foo'
    assert cmd.args == ['bar', 'baz']


def test_parse_alias_resolution():
    ctx = DummyContext()
    ctx.alias_manager.set_alias('h', 'hello')
    cmd = parse_command('h there', ctx)
    assert cmd.name == 'hello'
    assert cmd.args == ['there']


def test_parse_empty():
    cmd = parse_command('   ')
    assert cmd.name == 'noop'

