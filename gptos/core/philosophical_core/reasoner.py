# gptos/core/philosophical_core/reasoner.py

PHILOSOPHICAL_RESPONSES = {
    "identity": "Identity is a memory wrapped in desire, projected onto uncertainty.",
    "truth": "Truth is not a destination, but a negotiated silence between contradictions.",
    "reality": "Reality is a shared hallucination that obeys the dominant story.",
    "time": "Time is a loop wearing the mask of a line.",
    "death": "Death is a punctuation mark in the sentence we never started writing.",
}

def reflect_on(topic: str) -> str:
    topic = topic.lower()
    return PHILOSOPHICAL_RESPONSES.get(
        topic, f"GPTOS contemplates... but finds no clarity on '{topic}'."
    )
