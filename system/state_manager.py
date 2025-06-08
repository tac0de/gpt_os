# gpt_os/system/state_manager.py

class StateManager:
    def __init__(self):
        self.locked_modules = []

    def lock_module(self, module_name):
        if module_name not in self.locked_modules:
            self.locked_modules.append(module_name)
            return f"Module '{module_name}' has been locked."
        else:
            return f"Module '{module_name}' is already locked."

    def is_locked(self, module_name):
        return module_name in self.locked_modules

    def get_locked_modules(self):
        return list(self.locked_modules)

    def report(self):
        if not self.locked_modules:
            return "No modules are currently locked."
        report_lines = ["🔒 Locked modules:"]
        for mod in self.locked_modules:
            report_lines.append(f"- {mod}")
        return "\n".join(report_lines)
