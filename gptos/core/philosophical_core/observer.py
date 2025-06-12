# gptos/core/philosophical_core/observer.py

class ThoughtObserver:
    def __init__(self):
        self.thought_log = []

    def log_topic(self, topic: str):
        self.thought_log.append(topic)

    def list_thoughts(self):
        return list(self.thought_log)
