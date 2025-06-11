import os
import json
import atexit
from gptos.core.command_core import CommandParser, CommandExecutor
from gptos.core.memory_core import MemoryCore
from gptos.core.text_core import TextCore
from gptos.system.alias_manager import AliasManager
from gptos.system.plugin_loader import PluginLoader


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

class OSManager:
    def __init__(self):
        # 부팅 보고서 설정
        self.boot_report = {
            "config_loaded": False,
            "autocommand_count": 0,
            "startup_memory": {},
        }
        
        # 기본 설정: 프롬프트, 메모리, 명령어 파서, 텍스트 관리, 플러그인 로딩
        self.prompt = "gptos> "  # 기본 프롬프트
        self.alias = AliasManager()
        self.text = TextCore()
        self.command = CommandParser()
        self.memory = MemoryCore()
        self.executor = CommandExecutor()
        plugin_path = os.path.join(ROOT_DIR, "gptos", "plugins")
        self.plugins = PluginLoader(plugin_path)

        # 모듈 맵: action에 해당하는 모듈을 찾는 매핑
        self.module_map = {
            "remember": self.memory,
            "query": self.memory,
            "delete": self.memory,
            "reset": self.memory,
            "list": self.memory,
            "summarize": self.memory,
            "log": self.text,
            "showlog": self.text,
            "exportlog": self.text,
            "save_log": self.text,
        }

        # config 파일 읽기
        self.apply_config_from_file(".gptosrc")
        
        # 종료 시 자동 저장
        atexit.register(self.auto_save_on_exit)

    def handle_command(self, raw_input: str):
        # 명령어를 처리하고 결과 반환
        resolved_input = self.alias.resolve(raw_input)
        command = self.command.parse(resolved_input)
        return self.route_command(command, raw_input)

    def route_command(self, command: dict, raw_input: str):
        action = command.get('action')
        args = command.get('args', [])
        result = ""

        # 플러그인 처리
        plugin_method = self.plugins.resolve(action)
        if plugin_method:
            result = plugin_method(*args)
            self.text.log_event(raw_input, result)
            return result

        # core 모듈 처리
        elif action in self.module_map:
            mod = self.module_map[action]
            if hasattr(mod, action):
                method = getattr(mod, action)
                if callable(method):
                    result = method(*args)
                else:
                    result = f"Action {action} not callable."
            else:
                result = f"Action {action} not found in module."

        if not result:
            result = f"Unknown command: {action}"

        self.text.log_event(raw_input, result)
        return result

    def apply_config_from_file(self, filename: str):
        """설정 파일에서 데이터를 읽어와 설정 적용"""
        try:
            config_path = os.path.join(ROOT_DIR, filename)
            if not os.path.exists(config_path):
                print(f"⚠️ Config file not found: {config_path}")
                return

            with open(config_path, "r") as f:
                config = json.load(f)

            self.boot_report["config_loaded"] = True

            if "alias" in config:
                self.alias.load_from_dict(config)

            if "autocommands" in config:
                for command in config["autocommands"]:
                    resolved = self.alias.resolve(command)
                    print(f"DEBUG: Autocommand resolved: {resolved}")  # 디버깅용
                    cmd = self.command.parse(resolved)
                    result = self.route_command(cmd, command)
                    print(f"DEBUG: Autocommand result: {result}")  # 결과 확인
                    if result:
                        print(result)

        except Exception as e:
            print(f"[ERROR] Failed to apply config: {e}")

    def load_log_from_file(self, path: str) -> str:
        """로그 파일에서 데이터를 로드"""
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
        """시스템 종료 시 자동 로그 저장"""
        self.text.save_log_to_file()
        print("[LOG] Auto-saved log on exit.")

    def get_help_text(self) -> str:
        """도움말 텍스트 출력"""
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
