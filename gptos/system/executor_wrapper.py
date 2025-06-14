from gptos.core.command_core.parser import parse_command
from gptos.core.command_core.executor import execute

def executor_fn(raw_input: str, context):
    try:
        command = parse_command(raw_input)
        return execute(command, context)
    except Exception as e:
        print(f"[REPLAY ERROR] Failed to execute: {e}")
        return None
