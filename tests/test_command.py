# tests/test_command.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.command_core import CommandParser

parser = CommandParser()

def test_remember_command_parsing():
    cmd = parser.parse('remember name "Yuna"')
    assert cmd == {"action": "remember", "args": ["name", "Yuna"]}

def test_query_command():
    cmd = parser.parse('query "What is my name?"')
    assert cmd == {"action": "query", "args": ["What is my name?"]}

def test_empty_input():
    cmd = parser.parse('')
    assert cmd == {"action": None, "args": []}

def test_unquoted_argument():
    cmd = parser.parse('remember goal LearnPython')
    assert cmd == {"action": "remember", "args": ["goal", "LearnPython"]}

def test_partial_quotes():
    cmd = parser.parse('remember topic "OpenAI GPT')
    assert cmd == {"action": "remember", "args": ["topic", "OpenAI GPT"]}
