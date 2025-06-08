# gpt_os/interface/io_adapter.py

class IOAdapter:
    def __init__(self):
        self.input_mode = "cli"
        self.output_mode = "cli"

    def read(self):
        """
        Read user input based on current mode.
        Currently CLI-only.
        """
        try:
            return input(">>> ").strip()
        except EOFError:
            return "exit"

    def write(self, message):
        """
        Output message based on current output mode.
        """
        if self.output_mode == "cli":
            print(message)
        else:
            # Future modes: json, GUI, web
            print(f"[{self.output_mode}] {message}")
