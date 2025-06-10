# tests/test_memory.py
# tests/test_memory.py
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.memory_core import MemoryCore


@pytest.fixture
def mem():
    return MemoryCore()

def test_remember_stores_value(mem):
    mem.remember("name", "Yuna")
    assert mem.query("name") == "Yuna"

def test_query_returns_not_found(mem):
    assert mem.query("unknown") == "[NOT FOUND]"

def test_reset_clears_memory(mem):
    mem.remember("goal", "Build GPT OS")
    mem.reset()
    assert mem.query("goal") == "[NOT FOUND]"

def test_get_all_returns_correct_dict(mem):
    mem.remember("a", "1")
    mem.remember("b", "2")
    all_data = mem.get_all()
    assert all_data == {"a": "1", "b": "2"}

def test_delete_existing_key(mem):
    mem.remember("temp", "data")
    assert mem.delete("temp") is True
    assert mem.query("temp") == "[NOT FOUND]"

def test_delete_nonexistent_key(mem):
    assert mem.delete("ghost") is False

def test_list_keys_returns_all_keys(mem):
    mem.remember("a", "1")
    mem.remember("b", "2")
    keys = mem.list_keys()
    assert set(keys) == {"a", "b"}

def test_list_keys_empty_after_reset(mem):
    mem.remember("x", "100")
    mem.reset()
    assert mem.list_keys() == []
