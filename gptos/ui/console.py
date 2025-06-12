from gptos.core.command_core.parser import parse_command
from gptos.core.command_core.executor import execute
from gptos.system.context_handler import SystemContext
from gptos.plugins.reload_plugin import load_plugins

def main():
    context = SystemContext()
    load_plugins()
    while True:
        raw_input_cmd = input(">>> ")
        if raw_input_cmd.strip() in ["exit", "quit"]:
            print("Shutting down GPT OS.")
            break
        command = parse_command(raw_input_cmd, context)
        context.log(command)
        execute(command, context)

if __name__ == "__main__":
    main()
