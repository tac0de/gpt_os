from datetime import datetime

def get_commands():
    return {
        "now": get_now,
        "date": get_date
    }

def get_now(*args):
    return datetime.now().strftime("🕒 %Y-%m-%d %H:%M:%S")

def get_date(*args):
    return datetime.now().strftime("📅 %A, %B %d, %Y")
