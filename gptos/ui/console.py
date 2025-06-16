from gptos.core.command_core.parser import parse_command
from gptos.core.command_core.executor import execute
from gptos.system.context_handler import SystemContext
from gptos.plugins.reload_plugin import load_plugins

# 🔥 추가 import
from gptos.core.memory_core.indexer import MemoryIndexer
from gptos.core.memory_core.rewriter import MemoryRewriter

def main():
    context = SystemContext()
    load_plugins()

    # ✅ 메모리 인덱서, 리라이터 연결
    context.memory_indexer = MemoryIndexer()
    context.memory_rewriter = MemoryRewriter(context)

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
