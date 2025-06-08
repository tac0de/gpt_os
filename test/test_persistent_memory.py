import unittest
import os
import json
from core.memory_core import MemoryCore

TEST_STORAGE_PATH = "tests/temp_memory.json"

class TestPersistentMemoryCore(unittest.TestCase):
    def setUp(self):
        # Clean previous test memory
        if os.path.exists(TEST_STORAGE_PATH):
            os.remove(TEST_STORAGE_PATH)
        self.memory = MemoryCore(storage_path=TEST_STORAGE_PATH)

    def test_persistence_store_and_load(self):
        self.memory.remember("test_key", "test_value")
        self.assertEqual(self.memory.recall("test_key"), "test_value")

        # Create a new instance and ensure it loads same data
        memory2 = MemoryCore(storage_path=TEST_STORAGE_PATH)
        self.assertEqual(memory2.recall("test_key"), "test_value")

    def tearDown(self):
        if os.path.exists(TEST_STORAGE_PATH):
            os.remove(TEST_STORAGE_PATH)

if __name__ == '__main__':
    unittest.main()