# gpt_os/commands/api_test.py

def test_command(command_core, command_line):
    """
    Run a simulated command line input against the CommandCore.

    Args:
        command_core: instance of CommandCore
        command_line: raw string command (e.g., "remember color blue")
    """
    print(">>> Testing CommandCore Execution")
    print(f"Input: {command_line}")
    output = command_core.execute(command_line)
    print(f"Output: {output}")
    return output


def test_memory(memory_core):
    print(">>> Testing MemoryCore")
    print(memory_core.remember("test_key", "test_value"))
    print(memory_core.recall("test_key"))
    print(memory_core.forget("test_key"))
    print(memory_core.recall("test_key"))


def test_image(image_core):
    print(">>> Testing ImageCore")
    prompt = image_core.recommend_prompt("고양이")
    print(f"Recommended prompt: {prompt}")
    print(image_core.generate_image(prompt))


def test_philosophy(philosophy_core):
    print(">>> Testing PhilosophyCore")
    print(philosophy_core.reflect("나는 누구인가?"))
    print(philosophy_core.meta_infer("이 말은 거짓이다"))
