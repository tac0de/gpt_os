# GPT OS (v0.1.0)

🧠 A minimal ethical operating system for the terminal, written in Python.  
GPT OS is a modular, memory-enabled, plugin-driven command-line interface  
designed to reflect on commands, enforce rules, and think with you.

---

## ✅ Features

- 🔧 Modular plugin system (`reload`, `config`, `help`, `alias`, etc.)
- 🧠 Memory engine to log and summarize user inputs
- ⚖️ Ethics enforcement via `@ethics_guard` system
- 🤔 Built-in philosophical reflection core
- 🔁 Hot plugin reloading (no restart needed)
- 🛠 Devtools for simulation, echo, and plugin inspection

---

## 📦 Installation

```bash
pip install -e .
```

Once installed, run:

```bash
gptos
```

---

## 🚀 Sample Commands

```bash
>>> hello
>>> memory
>>> config strict_mode off
>>> alias hi=hello
>>> hi
>>> question what is reality
>>> thoughts
>>> status
>>> reload
>>> help
```

---

## 🧩 Supported Commands

| Command       | Description                                      |
|---------------|--------------------------------------------------|
| `hello`       | Sanity check plugin                              |
| `memory`      | Summarize recent commands                        |
| `config`      | Get/set system config (e.g., `strict_mode`)      |
| `alias`       | Create command aliases (e.g., `alias hi=hello`)  |
| `question`    | Ask philosophical questions                      |
| `thoughts`    | Show all past questions                          |
| `reload`      | Reload all plugin files live                     |
| `status`      | Print system state summary                       |
| `help`        | List all active commands                         |
| `dev`         | Developer tools: echo, simulate, inspect         |

---

## 📁 Architecture

GPT OS is organized into:

- `core/` — memory, command, philosophy, text
- `plugins/` — one file per command (autoloaded)
- `system/` — context manager, ethics, alias
- `ui/console.py` — the REPL entrypoint

---

## 🛡️ Ethics Mode

Ethics is strictly enforced by default.

```bash
>>> config strict_mode off  # to disable
```

This guards against unsafe or manipulative behavior, and is audited by:

```bash
>>> ethics
```

---

## 🔩 Extending GPT OS

To add a new plugin:

1. Create a new file `yourplugin_plugin.py` in `gptos/plugins/`
2. Define a `PLUGIN_REGISTRY = { "yourcommand": YourPluginClass() }`
3. Implement `register()` and `execute()` methods
4. Use `reload` to activate it live

---

© 2025 Wonyoung Choi  
MVP internal release – Not yet production hardened