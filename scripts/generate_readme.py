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
    try:
        with open("setup.cfg") as f:
            for line in f:
                if line.startswith("version ="):
                    return line.split("=")[-1].strip()
    except:
        return "0.0.0"

def generate_readme():
    plugins = get_plugins()
    version = read_version()
    date = datetime.today().strftime("%Y-%m-%d")

    readme = f"""# 🧠 GPT OS

Modular command interface powered by plugins and prompt-driven code generation.  
**Version**: `{version}`  **Last Updated**: {date}

---

## 🔌 Available Plugins

"""
    for p in plugins:
        readme += f"- `{p}`\n"

    readme += """

---

## 🧰 Getting Started

```bash
git clone https://github.com/tac0de/gpt_os.git
cd gpt_os
pip install -e .
gptos
📄 License
MIT License. See LICENSE.
"""

if __name__ == "__main__":
    try:
        generate_readme()
    except Exception as e:
        print(f"❌ Error: {e}")
