import unittest
from core.philosophy_core import PhilosophyCore

class TestPhilosophyCore(unittest.TestCase):
    def setUp(self):
        self.phil = PhilosophyCore()

    def test_reflect_responds(self):
        result = self.phil.reflect(["What", "is", "truth?"])
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_meta_infer_responds(self):
        result = self.phil.meta_infer(["GPT", "OS", "structure"])
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main()