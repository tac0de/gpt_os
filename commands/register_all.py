# gpt_os/commands/register_all.py

def register_all_commands(command_core, modules):
    """
    Register all commands from various modules into the CommandCore.

    Args:
        command_core (CommandCore): the command handler
        modules (dict): named modules (e.g., {"memory": MemoryCore(), ...})
    """

    # Memory commands
    memory = modules.get("memory")
    if memory:
        command_core.register("remember", lambda args: memory.remember(*args), "Store a key-value pair in memory")
        command_core.register("recall", lambda args: memory.recall(*args), "Retrieve value from memory")
        command_core.register("forget", lambda args: memory.forget(*args), "Delete a memory entry")
        command_core.register("list-memory", lambda args: memory.list_memory(), "List all stored memory")

    # Text parsing example (can be expanded later)
    text = modules.get("text")
    if text:
        command_core.register("parse", lambda args: text.parse(" ".join(args)), "Apply natural language parsing to input")

    # Image generation
    image = modules.get("image")
    if image:
        command_core.register("generate-image", lambda args: image.generate_image(" ".join(args)), "Generate image from prompt")
        command_core.register("recommend-prompt", lambda args: image.recommend_prompt(" ".join(args)), "Suggest a visual prompt")

    # Philosophy reflection
    philosophy = modules.get("philosophy")
    if philosophy:
        command_core.register("reflect", lambda args: philosophy.reflect(" ".join(args)), "Philosophical reflection")
        command_core.register("meta-infer", lambda args: philosophy.meta_infer(" ".join(args)), "Logical/meta paradox resolution")
    # Register all commands into the core
    code = modules.get('code')
    if code:
        command_core.register(
            "evaluate",
            lambda args: code.evaluate(" ".join(args)),
            "Evaluate a Python expression and return the result"
        )
        command_core.register(
            "execute",
            lambda args: code.execute(" ".join(args)),
            "Execute Python code block and show printed output"
        )


    # Debug/test commands can be added here

    command_core.register("whoami", lambda args: "You are running GPT OS.", "Identity check")
