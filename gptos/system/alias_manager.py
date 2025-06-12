class AliasManager:
    def __init__(self):
        self.aliases = {}

    def define(self, alias, target):
        self.aliases[alias] = target

    def resolve(self, command_name):
        return self.aliases.get(command_name, command_name)

    def list_aliases(self):
        return self.aliases
