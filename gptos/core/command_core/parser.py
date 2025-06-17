from typing import Optional

class Command:
    def __init__(self, name: str, args: Optional[list] = None, raw_input: Optional[str] = None):
        self.name = name
        self.args = args or []
        self.raw = raw_input  # 🔥 Needed for logging and replay

def parse_command(raw_input: str, context: Optional[object] = None) -> Command:
    """
    Parses a raw command string into a Command object.
    If context has alias_manager, resolves command alias.
    """
    parts = raw_input.strip().split()
    if not parts:
        return Command(name="noop", raw_input=raw_input)

    command_name = parts[0]
    args = parts[1:]

    # Safe alias resolution if context has alias_manager
    if context and hasattr(context, "alias_manager") and callable(getattr(context.alias_manager, "resolve", None)):
        command_name = context.alias_manager.resolve(command_name)

    return Command(name=command_name, args=args, raw_input=raw_input)