import unittest
from gptos.system.os_manager import OSManager

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.os_manager = OSManager()  # OSManager 객체 생성

    def test_autocommand(self):
        # 메모리에 데이터를 추가
        self.os_manager.handle_command("remember key1 value1")
        result = self.os_manager.handle_command("summarize")
        print(f"DEBUG: Autocommand result: {result}")
        self.assertIn("summarize", result)  # 'summarize'가 포함되어야 합니다.


    def test_mem(self):
        result = self.os_manager.handle_command("summarize")  # 'mem' 대신 'summarize'
        print(f"DEBUG: Summarize result: {result}")
        self.assertIn("summarize", result)  # 'summarize'가 포함되어야 합니다.

    def test_calc(self):
        result = self.os_manager.handle_command("calc 2 + 2")
        print(f"DEBUG: Calc result: {result}")
        self.assertIn("Result: 4", result)

    def test_genimg(self):
        result = self.os_manager.handle_command("genimg test_image")
        print(f"DEBUG: Genimg result: {result}")
        self.assertIn("Image saved", result)  # 'Image saved'가 출력될 것으로 예상
