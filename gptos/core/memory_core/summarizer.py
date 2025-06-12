def summarize_memory(context, limit=10):
    """Return a textual summary of recent commands."""
    summary = context.memory[-limit:]
    return "\n".join(f"{i+1}. {cmd.name} {cmd.args}" for i, cmd in enumerate(summary))
