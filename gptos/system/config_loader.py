import os

def get_project_root() -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

def get_gptos_dir() -> str:
    path = os.path.join(get_project_root(), ".gptos")
    os.makedirs(path, exist_ok=True)
    return path

def get_alias_file_path() -> str:
    return os.path.join(get_gptos_dir(), "aliases.json")