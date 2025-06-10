# tests/test_text.py

import sys
import os
import io
from contextlib import redirect_stdout

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.text_core import TextCore

def test_format_output():
    text = TextCore()
    result = text.format_output("query", "Yuna")
    assert result == "[QUERY]\nYuna"  # ✅ 줄바꿈 포함

def test_format_kv():
    text = TextCore()
    result = text.format_kv("name", "Yuna")
    assert result == "name → Yuna"

def test_log_event_and_clear_log():
    text = TextCore()
    text.log_event("query name", "Yuna")
    assert len(text.log_history) == 1
    assert "query name" in text.log_history[0]
    text.clear_log()
    assert text.log_history == []

def test_print_log_outputs_to_console():
    text = TextCore()
    text.log_event("remember goal", "Build OS")

    f = io.StringIO()
    with redirect_stdout(f):
        text.print_log()
    output = f.getvalue()

    assert "[SESSION LOG]" in output
    assert "remember goal" in output

def test_export_log_returns_valid_json(tmp_path):
    text = TextCore()
    text.log_event("remember user", "Yuna")
    json_str = text.export_log()
    
    import json
    data = json.loads(json_str)
    assert isinstance(data, list)
    assert "timestamp" in data[0]
    assert "command" in data[0]
    assert "output" in data[0]

def test_save_log_to_file_creates_file(tmp_path):
    text = TextCore()
    text.log_event("remember lang", "Python")

    file_path = tmp_path / "logs.json"
    message = text.save_log_to_file(str(file_path))
    
    assert file_path.exists()
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        assert "Python" in content
    assert "successfully" in message
