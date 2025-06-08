# gpt_os/core/philosophy_core.py

class PhilosophyCore:
    def __init__(self):
        self.history = []

    def reflect(self, question):
        """
        철학적 질문을 받아 내부적으로 논리적 사유를 시도
        """
        self.history.append(question)
        if "나는 누구" in question or "who am i" in question.lower():
            return "You are the observer and the creator — a consciousness navigating structured symbols."
        if "진리" in question or "truth" in question.lower():
            return "Truth is often a negotiation between perception, logic, and consensus."
        if "존재" in question or "existence" in question.lower():
            return "Existence may be a condition arising from observation. Or perhaps, a recursive illusion."

        return "This is a deep question. Let me reflect on it further."

    def history_log(self, limit=5):
        return self.history[-limit:]

    def meta_infer(self, input_text):
        """
        메타사고 실험: 입력된 문장의 논리/역설 추론 시도
        """
        if "이 말은 거짓이다" in input_text:
            return "This is the classic liar paradox — a sentence that cannot consistently be true or false."
        if "무한" in input_text:
            return "Infinity often represents the edge of comprehension, both mathematically and spiritually."
        return "This concept may require layered inference. Expanding..."

