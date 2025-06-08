# gpt_os/system/debug_tools.py

def debug_status(state_manager, command_core, memory_core=None, logger=None):
    """
    Print high-level debug overview of the GPT OS state.
    """
    lines = []

    # Locked modules
    locked = state_manager.get_locked_modules()
    lines.append("🔒 Locked Modules:")
    lines.extend(f"- {mod}" for mod in locked)

    # Available commands
    lines.append("\n⚙️ Registered Commands:")
    for cmd in sorted(command_core.commands.keys()):
        desc = command_core.commands[cmd].get("description", "")
        lines.append(f"- {cmd}: {desc}")

    # Memory overview
    if memory_core:
        lines.append("\n🧠 Memory Slots:")
        memory_dump = memory_core.list_memory()
        lines.append(memory_dump)

    # Last logs
    if logger:
        lines.append("\n🪵 Last Logs:")
        lines.append(logger.last(3))

    return "\n".join(lines)


def quick_log(logger, msg):
    """
    Log a message through the workflow logger (if available).
    """
    if logger:
        logger.log(f"[DEBUG] {msg}")
