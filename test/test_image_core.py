import unittest
from core.image_core import ImageCore

class TestImageCore(unittest.TestCase):
    def setUp(self):
        self.image_core = ImageCore()

    def test_generate_image_prompt(self):
        result = self.image_core.generate_image_prompt(["sunset", "forest"])
        self.assertIsInstance(result, str)
        self.assertTrue("sunset" in result.lower() or "forest" in result.lower())

    def test_recommend_prompt(self):
        result = self.image_core.recommend_prompt(["castle", "night"])
        self.assertIsInstance(result, str)
        self.assertTrue("castle" in result.lower() or "night" in result.lower())

if __name__ == '__main__':
    unittest.main()