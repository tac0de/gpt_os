# gptos/system/context_handler.py

import os
from gptos.system.alias_manager import AliasManager
from gptos.system.command_log import logger
from gptos.system.rag_pipeline import SimpleRAGPipeline, load_default_rag_docs

class SystemContext:
    def __init__(self):
        self.memory = []
        self.config = {
            "strict_mode": True,
            "log.level": "INFO",
            "memory.dedup": True,
            "summarize.recent_count": 10,
        }
        self.alias_manager = AliasManager()
        self.logger = logger  # Optional, in case access needed
        self.rag_pipeline = SimpleRAGPipeline()
        self.rag_pipeline.add_documents([
            "GPT OS is a modular system for language interface research.",
            "RAG stands for Retrieval Augmented Generation.",
            "This system is optimized for prompt-based workflows.",
            "You can query internal memory using the /rag endpoint."
        ])

    def log(
        self,
        command,
        *,
        parsed=None,
        result=None,
        error=None,
        status=None,
        duration=None,
        plugin=None,
    ):
        from gptos.core.memory_core.recorder import record_command
        record_command(self, command)

        self.logger.log(
            raw_input=command.raw,
            parsed=parsed,
            result=result,
            error=error,
            status=status,
            duration=duration,
            plugin=plugin,
        )

def create_system_context():
    ctx = SystemContext()

    # RAG 초기화 및 문서 로딩
    ctx.rag_pipeline = SimpleRAGPipeline()
    load_default_rag_docs(ctx.rag_pipeline)

    return ctx
