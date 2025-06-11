# core/command_core.py

from gptos.core.memory_core import MemoryCore

class CommandParser:
    def parse(self, raw_input: str) -> dict:
        tokens = raw_input.strip().split()
        if not tokens:
            return {'action': None, 'args': []}
        action = tokens[0].lower()
        args = self._group_arguments(tokens[1:])
        return {'action': action, 'args': args}

    def _group_arguments(self, tokens: list) -> list:
        args = []
        buffer = []
        in_quotes = False

        for token in tokens:
            if token.startswith('"') or token.startswith("'"):
                in_quotes = True
                buffer = [token.lstrip('"\'')]
            elif token.endswith('"') or token.endswith("'"):
                buffer.append(token.rstrip('"\''))
                args.append(' '.join(buffer))
                buffer = []
                in_quotes = False
            elif in_quotes:
                buffer.append(token)
            else:
                args.append(token)

        if buffer:  # if unclosed quote, just join as-is
            args.append(' '.join(buffer).rstrip('"\''))
        return args



class CommandExecutor:
    def __init__(self):
        self.memory = MemoryCore()

    def execute(self, command: dict):
        action = command.get('action')
        args = command.get('args', [])

        if action == "remember" and len(args) >= 2:
            key, value = args[0], args[1]
            self.memory.remember(key, value)
        elif action == "query" and len(args) >= 1:
            key = args[0]
            result = self.memory.query(key)
            print(f"[QUERY] {key} → {result}")
        elif action == "reset":
            self.memory.reset()
        elif action == "log":
            all_memory = self.memory.get_all()
            print("[MEMORY LOG]")
            for k, v in all_memory.items():
                print(f"  {k} → {v}")
        else:
            print(f"[ERROR] Unknown or malformed command: {action}")
