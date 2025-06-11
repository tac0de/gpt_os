def get_commands():
    return {
        "hello": say_hello
    }

def say_hello(*args):
    name = args[0] if args else "world"
    return f"Hello, {name}!"
