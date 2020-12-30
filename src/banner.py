import json

from src import colors

class htotw:
    data = None

def load():
    with open("htotw.json", 'r') as f:
        htotw.data = json.load(f)

def description():
    return ("%s%s%s" % (
        colors.get("blue", 3),
        htotw.data["description"],
        colors.get("reset", 0)))

def display():
    print("┌───────────────────────────────────────────────────┐")
    print("│                                                   │")
    print("│  888  888 888888888 88888888 888888888 8d8   d88  │")
    print("│  88888888    '88d   888  888    '88d   888,o.d88  │")
    print("│  88P  888   '888    888  888   '888    888P`Y8b8  │")
    print("│  88P  888 '88p      888oo888 '88p      88P   YP8  │")
    print("│                                                   │")
    print("│  %s                   %sv%s%s  │" % (description(),
        colors.get("cyan", 3), htotw.data["version"], colors.get("reset", 0)))
    print("└───────────────────────────────────────────────────┘", end = "\n\n")