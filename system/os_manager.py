import os
import json
import atexit
from core.command_core import CommandParser, CommandExecutor
from core.memory_core import MemoryCore
from core.text_core import TextCore

class OSManager:
    def __init__(self):
        self.text = TextCore()
        self.command = CommandParser()
        self.memory = MemoryCore()
        self.executor = CommandExecutor()
        self.apply_config_from_file(".gptosrc")
        atexit.register(self.auto_save_on_exit)

    def handle_command(self, raw_input: str):
        command = self.command.parse(raw_input)
        return self.route_command(command, raw_input)

    def route_command(self, command: dict, raw_input: str):
        action = command.get('action')
        args = command.get('args', [])
        result = ""

        try:
            if action == "remember" and len(args) >= 2:
                self.memory.remember(args[0], args[1])
                result = self.text.format_output("memory", f"Remembered {args[0]} → {args[1]}")

            elif action == "query" and len(args) >= 1:
                value = self.memory.query(args[0])
                result = self.text.format_output("query", self.text.format_kv(args[0], value))

            elif action == "reset":
                self.memory.reset()
                result = self.text.format_output("memory", "Memory reset")

            elif action == "log":
                result = self.text.format_output("memory", "Printing memory log:")
                print(result)
                for k, v in self.memory.get_all().items():
                    print(" ", self.text.format_kv(k, v))
                return self.text.log_event(raw_input, "[PRINTED MEMORY LOG]")

            elif action == "showlog":
                self.text.print_log()
                return

            elif action == "delete" and len(args) >= 1:
                success = self.memory.delete(args[0])
                if success:
                    result = self.text.format_output("memory", f"Deleted {args[0]}")
                else:
                    result = self.text.format_output("memory", f"{args[0]} not found")

            elif action == "list":
                keys = self.memory.list_keys()
                if keys:
                    result = self.text.format_output("memory", f"Stored keys: {', '.join(keys)}")
                else:
                    result = self.text.format_output("memory", "No keys stored.")

            elif action == "summarize":
                pairs = self.memory.memory.items()
                if pairs:
                    lines = [self.text.format_kv(k, v) for k, v in pairs]
                    result = self.text.format_output("memory", "\n".join(lines))
                else:
                    result = self.text.format_output("memory", "No memory stored.")

            elif action == "exportlog":
                json_log = self.text.export_log()
                result = self.text.format_output("log", json_log)

            elif action == "save_log":
                msg = self.text.save_log_to_file()
                result = self.text.format_output("log", msg)

            elif action == "import_log":
                path = args[0] if args else "logs.json"
                msg = self.load_log_from_file(path)
                result = self.text.format_output("log", msg)

            elif action == "help":
                result = self.text.format_output("help", self.get_help_text())
            elif action == "version":
                result = self.text.format_output("system", "GPT OS v0.1 – powered by wonyoung")


            elif action in ["exit", "quit"]:
                exit(0)

            else:
                result = self.text.format_output("error", f"Unknown command: {action}")

            # 로그 기록
            self.text.log_event(raw_input, result)
            return result

        except Exception as e:
            error_msg = self.text.format_output("error", str(e))
            self.text.log_event(raw_input, error_msg)
            return error_msg

    def apply_config_from_file(self, filename: str):
        try:
            config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", filename))
            if not os.path.exists(config_path):
                return

            with open(config_path, "r", encoding="utf-8") as f:
                config = json.load(f)

            if "autoload_log" in config:
                self.load_log_from_file(config["autoload_log"])

            if "startup_memory" in config:
                for key, value in config["startup_memory"].items():
                    self.memory.remember(key, value)

            if "autocommands" in config:
                for raw in config["autocommands"]:
                    cmd = self.command.parse(raw)
                    result = self.route_command(cmd, raw)
                    if result:
                        print(result)  # ✅ 출력 보장


        except Exception as e:
            print(f"[ERROR] Failed to apply config: {e}")

    def load_log_from_file(self, path: str) -> str:
        if not os.path.exists(path):
            return f"File not found: {path}"

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        count = 0
        for entry in data:
            if "command" in entry and entry["command"].startswith("remember"):
                try:
                    _, key, value = entry["command"].split(maxsplit=2)
                    self.memory.remember(key, value)
                    count += 1
                except Exception:
                    continue

        return f"Restored {count} memory entries from {path}"

    def auto_save_on_exit(self):
        self.text.save_log_to_file()
        print("[LOG] Auto-saved log on exit.")

    def get_help_text(self) -> str:
        return (
            "Available commands:\n"
            "  remember <key> <value>    - Store a memory value\n"
            "  query <key>               - Retrieve a memory\n"
            "  summarize                 - Summarize all stored memory\n"
            "  delete <key>              - Remove a memory\n"
            "  list                      - List stored keys\n"
            "  reset                     - Clear all memory\n"
            "  log                       - Print current memory log\n"
            "  showlog                   - Display full command log\n"
            "  exportlog                 - Export log as JSON\n"
            "  save_log                  - Save current session log to file\n"
            "  import_log [file]         - Restore memory from log\n"
            "  help                      - Show this help message\n"
            "  exit / quit               - Exit the OS\n"
        )
