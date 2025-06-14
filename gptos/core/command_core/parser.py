

class Command:
    def __init__(self, name, args=None, raw_input = None):
        self.name = name
        self.args = args or []
        self.raw = raw_input  # 🔥 Needed for logging and replay
        
def parse_command(raw_input: str, context=None) -> 'Command':
    parts = raw_input.strip().split()
    if not parts:
        return Command(name="noop", raw_input=raw_input)
    
    command_name = parts[0]
    if context:
        command_name = context.alias_manager.resolve(command_name)

    return Command(name=command_name, args=parts[1:], raw_input=raw_input)


