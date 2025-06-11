from gptos.core.image_core import ImageCore

image = ImageCore()

def genimg(*args):
    name = args[0] if args else "image"
    return image.generate_placeholder(name)

def ascii(*args):
    if not args:
        return "[ERROR] Provide text to convert"
    text = " ".join(args)
    return image.text_to_ascii(text)

def imagelist(*args):
    files = image.list_images()
    if not files:
        return "No images found."
    return "\n".join(files)

def imagemeta(*args):
    if not args:
        return "[ERROR] Provide filename"
    meta = image.get_image_metadata(args[0])
    if isinstance(meta, str):
        return meta
    return "\n".join(f"{k}: {v}" for k, v in meta.items())

def get_commands():
    return {
        "genimg": genimg,
        "ascii": ascii,
        "imagelist": imagelist,
        "imagemeta": imagemeta
    }

