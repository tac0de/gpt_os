import os

def get_api_key(config: dict, key: str, env_var: str, fallback: str = "") -> str:
    # 1. Try config first
    if key in config:
        return config[key]
    # 2. Then environment
    if env_var in os.environ:
        return os.environ[env_var]
    # 3. Then fallback
    return fallback
