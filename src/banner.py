import json

from src import colors

class htotw:
    data = None

def load():
    with open("htotw.json", 'r') as f:
        htotw.data = json.load(f)

def display():
    print("888  888 888888888 88888888 888888888 8d8   d88")
    print("88888888    '88d   888  888    '88d   888,o.d88")
    print("88P  888   '888    888  888   '888    888P`Y8b8")
    print("88P  888 '88p      888oo888 '88p      88P   YP8", end = "\n\n")

    print("%s%s %s%s" % (
        colors.get("red", 1),
        htotw.data["description"],
        htotw.data["version"],
        colors.get("reset", 0)),
        end = "\n\n")