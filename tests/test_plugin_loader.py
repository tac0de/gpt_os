import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from gptos.system.plugin_loader import load_plugins, PLUGIN_REGISTRY

def test_load_plugins_includes_hello():
    load_plugins()
    assert 'hello' in PLUGIN_REGISTRY
    assert callable(getattr(PLUGIN_REGISTRY['hello'], 'execute'))

