# gpt_os/core/image_core.py

class ImageCore:
    def __init__(self):
        self.default_size = "1024x1024"
        self.history = []

    def generate_image(self, prompt, size=None):
        """
        이미지 생성 요청 처리
        실제 API 연결은 추후 구현
        """
        final_size = size or self.default_size
        image_info = {
            "prompt": prompt,
            "size": final_size
        }
        self.history.append(image_info)

        # 실제 렌더링은 외부 툴/플러그인 연동 필요
        return f"[이미지 요청] Prompt: '{prompt}', Size: {final_size}"

    def recommend_prompt(self, user_input):
        """
        사용자 입력 기반 추천 prompt 생성
        (예: "고양이" → "a realistic 3D render of a cyberpunk cat")
        """
        if "고양이" in user_input:
            return "a realistic 3D render of a cyberpunk cat"
        elif "지도" in user_input or "map" in user_input:
            return "an old parchment-style fantasy world map with mountains and seas"
        return f"simple concept art of {user_input}"

    def get_history(self, limit=5):
        return self.history[-limit:]
