# gpt_os/core/command_core.py

class CommandCore:
    def __init__(self, state_manager):
        self.commands = {}
        self.state_manager = state_manager

        # 기본 명령어 등록
        self.register("help", self.help_command, "List all available commands")
        self.register("apply", self.apply_command, "Lock a module into the GPT OS workflow")
        self.register("report", self.report_command, "Show system status or logs")

    def register(self, command_name, func, description=""):
        self.commands[command_name] = {
            "func": func,
            "description": description
        }

    def execute(self, input_line):
        parts = input_line.strip().split()
        if not parts:
            return "No command entered."
        command = parts[0]
        args = parts[1:]

        if command in self.commands:
            return self.commands[command]["func"](args)
        else:
            return f"Unknown command: {command}"

    # --- 기본 명령어 구현 ---

    def help_command(self, args):
        output = [
            "🧠 GPT OS Help Menu",
            "Use these commands in the prompt below:",
            "",
            "🔧 System Commands:"
        ]
        for cmd in sorted(self.commands.keys()):
            desc = self.commands[cmd].get("description", "")
            if cmd in ["help", "apply", "report", "whoami"]:
                output.append(f"  • {cmd:<15} → {desc}")

        output.append("\n🧠 Memory Commands:")
        for cmd in self.commands:
            if cmd.startswith("remember") or cmd in ["recall", "forget", "list-memory"]:
                desc = self.commands[cmd].get("description", "")
                output.append(f"  • {cmd:<15} → {desc}")

        output.append("\n🎨 Image Commands:")
        for cmd in self.commands:
            if cmd.startswith("generate-image") or cmd.startswith("recommend-prompt"):
                desc = self.commands[cmd].get("description", "")
                output.append(f"  • {cmd:<15} → {desc}")

        output.append("\n📜 Philosophy Commands:")
        for cmd in self.commands:
            if cmd.startswith("reflect") or cmd.startswith("meta-infer"):
                desc = self.commands[cmd].get("description", "")
                output.append(f"  • {cmd:<15} → {desc}")

        output.append("\n💻 Code Commands:")
        for cmd in self.commands:
            if cmd in ["evaluate", "execute"]:
                desc = self.commands[cmd].get("description", "")
                output.append(f"  • {cmd:<15} → {desc}")

        return "\n".join(output)


    def apply_command(self, args):
        if not args:
            return "Usage: apply <module_name>"
        module_name = args[0]
        self.state_manager.lock_module(module_name)
        return f"Module '{module_name}' has been applied (locked into workflow)."

    def report_command(self, args):
        return self.state_manager.report()
