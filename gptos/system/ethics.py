STRICT_MODE = True

def ethics_guard(fn):
    def wrapper(command, context, *args, **kwargs):
        if context.config.get("strict_mode", True):
            print("⚠️ Ethics Mode: Strict")
        return fn(command, context, *args, **kwargs)
    return wrapper

