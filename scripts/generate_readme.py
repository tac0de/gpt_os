import os
from datetime import datetime

def get_plugins():
    path = "gptos/plugins"
    if not os.path.exists(path):
        return []
    return sorted(set(
        f.replace("_plugin.py", "")
        for f in os.listdir(path)
        if f.endswith("_plugin.py") and not f.startswith("__")
    ))

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

    if "openai" in plugins:
        print("\n---\n")
        print("## 🤖 OpenAI Plugin (Optional)")
        print("This plugin enables GPT-powered command interaction using your OpenAI API key.\n")

        print("### Installation")
        print("```bash")
        print("pip install openai")
        print("```")
        print("Or if using optional dependencies:")
        print("```bash")
        print("pip install gptos[openai]")
        print("```")

        print("### Configuration")
        print("```bash")
        print("gptos >>> config set openai.api_key sk-xxxxxxxxxxxxxxxx")
        print("```")
        print("Or set it as an environment variable:")
        print("```bash")
        print("export OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx")
        print("```")

        print("### Usage")
        print("```bash")
        print("gptos >>> openai ask suggest a helpful tip for terminal productivity")
        print("```")

        print("> If no API key is configured, the plugin will skip execution and show a warning.\n")

    print("## 📄 License")
    print("MIT License. See [LICENSE](LICENSE).\n")

if __name__ == "__main__":
    try:
        generate_readme()
    except Exception as e:
        print(f"❌ Error: {e}")
