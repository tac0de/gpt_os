import os
from gptos.system.alias_manager import AliasManager
from gptos.system.command_log import command_logger
from gptos.system.rag_pipeline import SimpleRAGPipeline, load_default_rag_docs
import gc

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
        self.logger = command_logger  # Optional, in case access needed
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
        
         # 로그 기록 최적화
        if len(self.memory) > self.config['summarize.recent_count']:
            self.memory = self.memory[-self.config['summarize.recent_count']:]

        self.logger.log(
            raw_input=command.raw,
            parsed=parsed,
            result=result,
            error=error,
            status=status,
            duration=duration,
            plugin=plugin,
        )

    def clean_old_data(self):
        """오래된 데이터 삭제"""
        self.memory = [data for data in self.memory if not self.is_old(data)]
        print("Old data cleaned.")

    def is_old(self, data):
        """데이터가 오래된 것인지 확인하는 함수"""
        # 예시: 오래된 데이터는 30일 이상된 데이터라고 가정
        # 실제로는 각 데이터에 timestamp가 있어야 함
        return False  # 테스트용으로 False, 실제 구현시 날짜를 비교

    def optimize_memory(self):
        """가비지 컬렉션 최적화"""
        gc.collect()  # 가비지 컬렉션 강제로 호출
        print("Memory optimized via garbage collection.")

def create_system_context():
    ctx = SystemContext()

    # RAG 초기화 및 문서 로딩
    ctx.rag_pipeline = SimpleRAGPipeline()
    load_default_rag_docs(ctx.rag_pipeline)

    return ctx
