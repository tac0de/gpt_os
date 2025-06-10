import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import readline
from system.os_manager import OSManager
from termcolor import colored

def main():
    os = OSManager()

    print(colored("Welcome to GPT OS Console. Type 'help' to get started.\n", "cyan"))

    while True:
        try:
            command = input(colored(">>> ", "green"))
            if command.strip().lower() in ["exit", "quit"]:
                break
            elif command.strip().lower() == "clear":
                print("\033c", end="")  # ANSI clear screen
                continue

            output = os.handle_command(command)

            # Apply color per section
            if output.startswith("[MEMORY]"):
                print(colored(output, "yellow"))
            elif output.startswith("[QUERY"):
                print(colored(output, "cyan"))
            elif output.startswith("[LOG]"):
                print(colored(output, "magenta"))
            elif output.startswith("[HELP]"):
                print(colored(output, "white"))
            elif output.startswith("[LOG]"):
                print(colored(output, "magenta"))
            else:
                print(output)

        except KeyboardInterrupt:
            print("\nExiting GPT OS.")
            break

if __name__ == "__main__":
    main()