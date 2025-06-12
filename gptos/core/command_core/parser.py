class Command:
    def __init__(self, name, args=None):
        self.name = name
        self.args = args or []
        
def parse_command(raw_input: str, context=None) -> 'Command':
    parts = raw_input.strip().split()
    if not parts:
        return Command(name="noop")
    command_name = parts[0]
    if context:
        command_name = context.alias_manager.resolve(command_name)
    return Command(name=command_name, args=parts[1:])

