import unittest
import os
from gptos.system.plugin_loader import PluginLoader

class TestPluginLoader(unittest.TestCase):
    def setUp(self):
        plugin_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "gptos", "plugins"))
        self.loader = PluginLoader(plugin_path)

    def test_resolve_existing_plugin(self):
        plugin = self.loader.resolve("genimg")  # 'genimg' 플러그인 함수 존재해야 함
        self.assertTrue(callable(plugin))

    def test_resolve_nonexistent_plugin(self):
        plugin = self.loader.resolve("nonexist")
        self.assertIsNone(plugin)

    def test_is_async_check(self):
        plugin = self.loader.resolve("quote")  # quote 플러그인이 async def 인 경우
        if plugin:
            self.assertEqual(self.loader.is_async("quote"), plugin.__code__.co_flags & 0x80 != 0)
