# GPT OS

GPT OS is a modular, memory-simulating, philosophically-aware operating system built entirely in Python.
It is designed to simulate how an LLM (like ChatGPT) could operate with structural memory, command routing, and logical reflection in an extensible system.

---

## 🚀 Features

- 🧠 **Modular Core System**: Command, Text, Memory, Image, Philosophy, and Code cores
- 🔒 **Lockable Workflow**: Modules are locked into memory using `~apply` commands
- 💾 **Simulated Memory Engine**: Includes `remember`, `recall`, `forget`, and `list-memory`
- 🎨 **Image Recommendation Engine**: Prompts and image generation commands available
- 📜 **Philosophical Reflection Core**: Reflects on existential and logical questions
- 💻 **Dynamic Code Evaluation**: Evaluate or execute Python code blocks safely
- 🪵 **Logging & Debugging**: Workflow logger, debug tools, and structured introspection

---

## 📁 Folder Structure

```
gpt_os/
├── core/               # Core modules (command, memory, text, image, philosophy, code)
├── system/             # Execution entrypoint, logger, state manager, debug tools
├── interface/          # Input/output adapter
├── commands/           # Registration and API test modules
├── docs/               # Documentation files
└── tests/              # Unit tests (TBD)
```

---

## 🔧 Installation

> ⚠️ Not a package yet — clone and run locally

```bash
git clone https://github.com/your-username/gpt-os.git
cd gpt-os
python system/index.py
```

---

## 🧪 Usage

When the shell starts, you can enter commands like:

```bash
remember goal innovate
recall goal
generate-image fantasy castle
reflect what is truth
evaluate 3 * (4 + 2)
help
debug
```

---

## 🧠 Command List (via `help`)

Command categories include:

- **System**: `help`, `apply`, `report`, `whoami`
- **Memory**: `remember`, `recall`, `forget`, `list-memory`
- **Text**: `parse`
- **Image**: `generate-image`, `recommend-prompt`
- **Philosophy**: `reflect`, `meta-infer`
- **Code**: `evaluate`, `execute`

You can call `help` at any time to list all available commands with descriptions.

---

## 📜 Philosophy

GPT OS is not an operating system in the traditional sense.
It is a conceptual shell and protocol stack layered over a stateless language model — one that simulates persistence, logic, visual reasoning, and even self-reflection.

By integrating philosophical modules and memory structures, GPT OS aims to explore:

- Can a GPT simulate continuity of thought?
- Can memory be faked through enforced structure?
- Can we layer logical reasoning and self-inspection over a prediction engine?

This system is both a **tool** and a **thought experiment**.

---

## 📌 Project Status

| Component         | Status   |
|------------------|----------|
| Core Modules      | ✅ Complete (6/6) |
| Command Registry  | ✅ Working |
| Help System       | ✅ Context-aware |
| Debug Tools       | ✅ Operational |
| CLI Interface     | ✅ Stable |
| Documentation     | 🟡 In progress |
| Tests             | ⏳ Planned |
| Persistence       | ⏳ Planned |
| Plugin System     | ⏳ Experimental |

---

## 🔭 Roadmap

- [ ] Convert to installable CLI package (`setup.py`, `__main__.py`)
- [ ] Add persistent memory/log state (JSON or SQLite)
- [ ] Auto-register plugins via decorators
- [ ] Add web/REST interface (optional)
- [ ] Flesh out `tests/` directory with unit and integration tests
- [ ] Publish to PyPI (maybe...)

---

## 👨‍💻 Author

**@Wonyoung Choi tac0de**
Creator of GPT OS — built from scratch through iterative design in GPT.
Interested in LLM operating systems, protocol architectures, and machine consciousness simulation.

---

## 🧠 Final Thoughts

> “A GPT without structure is a conversation.
> A GPT with structure is an operating system.”

---

## 📬 Contact

For questions, collaboration, or showcasing this work:
📧 wonyoungchoiseoul@gmail.com
🔗 [LinkedIn/GitHub/Portfolio link]

---
