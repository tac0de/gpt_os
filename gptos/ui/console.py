import asyncio
from gptos.system.os_manager import OSManager

def start_console():
    try:
        os = OSManager()
        print("🧠 GPT OS console started. Type 'help' or 'exit'.")
        while True:
            try:
                line = input(os.prompt)
                if line.strip():
                    command = os.command.parse(os.alias.resolve(line))
                    print(f"DEBUG: Command resolved: {command}")  # 명령어 확인
                    result = os.route_command(command, line)  # 실제 명령어 실행
                    print(f"DEBUG: Command result: {result}")  # 명령어 처리 결과
                    if result:
                        print(result)  # 정상적으로 출력하는 부분
            except KeyboardInterrupt:
                break
    except Exception as e:
        print(f"[ERROR] Failed to start console: {e}")





