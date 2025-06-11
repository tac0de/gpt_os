import os
import datetime

class ImageCore:
    def __init__(self, output_dir="images"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def generate_placeholder(self, name="image"):
        filename = f"{name}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        path = os.path.join(self.output_dir, filename)
        with open(path, "w") as f:
            f.write("[Image Placeholder]")
        return f"📷 Image saved to {path}"
    
    def text_to_ascii(self, text: str, width: int = 40) -> str:
        lines = []
        line = ""
        for word in text.split():
            if len(line + " " + word) > width:
                lines.append(line)
                line = word
            else:
                if line:
                    line += " "
                line += word
        if line:
            lines.append(line)
        return "\n".join(lines)
    
    def list_images(self):
        files = os.listdir(self.output_dir)
        return [f for f in files if f.endswith(".txt")]

    def get_image_metadata(self, name):
        path = os.path.join(self.output_dir, name)
        if not os.path.exists(path):
            return f"[ERROR] File not found: {name}"
        stat = os.stat(path)
        return {
            "name": name,
            "size": stat.st_size,
            "modified": datetime.datetime.fromtimestamp(stat.st_mtime).isoformat()
        }


