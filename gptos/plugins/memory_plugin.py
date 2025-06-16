from gptos.plugins.base import GPTOSPlugin

class MemoryPlugin(GPTOSPlugin):
    name = "memory"

    def register(self, context): pass

    def execute(self, command, context):
        args = command.args

        if not args:
            self.print_usage()
            return

        subcommand = args[0]

        if subcommand == "list":
            self.handle_list(args[1:], context)

        elif subcommand == "index":
            self.handle_index(args[1:], context)

        elif subcommand == "rewrite":
            self.handle_rewrite(args[1:], context)

        else:
            print(f"[memory] Unknown subcommand: {subcommand}")
            self.print_usage()

    def handle_list(self, args, context):
        category = args[0] if args else None
        memory = context.memory or []

        if category:
            filtered = [m for m in memory if m.get("category") == category]
            for i, item in enumerate(filtered):
                print(f"[{i}] {item['text']}")
        else:
            for i, item in enumerate(memory):
                print(f"[{i}] ({item['category']}) {item['text']}")

    def handle_index(self, args, context):
        if len(args) < 2:
            print("[memory] Usage: memory index <category> <text>")
            return

        category, text = args[0], " ".join(args[1:])
        indexer = getattr(context, "memory_indexer", None)

        if not indexer:
            print("[memory] Error: memory_indexer not configured in context")
            return

        indexer.add_entry(category, text)
        print(f"[memory] Indexed → ({category}) {text}")

    def handle_rewrite(self, args, context):
        if len(args) < 2 or args[0] != "dedup":
            print("[memory] Usage: memory rewrite dedup <category>")
            return

        category = args[1]
        rewriter = getattr(context, "memory_rewriter", None)

        if not rewriter:
            print("[memory] Error: memory_rewriter not configured in context")
            return

        rewriter.deduplicate(category)
        print(f"[memory] Deduplicated → {category}")

    def print_usage(self):
        print("Usage: memory [list|index <category> <text>|rewrite dedup <category>]")


PLUGIN_REGISTRY = {
    "memory": MemoryPlugin()
}
