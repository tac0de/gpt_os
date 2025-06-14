import os
from datetime import datetime

def get_plugins():
    path = "gptos/plugins"
    if not os.path.exists(path):
        return []
    return sorted([
        f.replace("_plugin.py", "")
        for f in os.listdir(path)
        if f.endswith("_plugin.py") and not f.startswith("__")
    ])

def read_version():
    with open("setup.cfg") as f:
        for line in f:
            if line.startswith("version ="):
                return line.split("=")[-1].strip()
    return "0.0.0"

def generate_readme():
    plugins = get_plugins()
    version = read_version()
    date = datetime.today().strftime("%Y-%m-%d")

    print(f"# GPT OS\n")
    print(f"🧠 Modular command interface powered by plugins and prompt-driven code generation.\n")
    print(f"**Version**: `{version}`  **Last Updated**: {date}")
    print("\n---\n")

    print("## 🔌 Available Plugins")
    for p in plugins:
        print(f"- `{p}`")

    print("\n---\n")
    print("## 🧰 Getting Started")
    print("```bash")
    print("git clone https://github.com/tac0de/gpt_os.git")
    print("cd gpt_os")
    print("pip install -e .")
    print("gptos")
    print("```")

    print("\n## 📄 License")
    print("MIT License. See [LICENSE](LICENSE).\n")

if __name__ == "__main__":
    try:
        generate_readme()
    except Exception as e:
        print(f"❌ Error: {e}")
