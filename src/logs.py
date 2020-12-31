from src import colors
from src import time

def action(message):
    print("%s%s%s" % (colors.get("blue", 1), message, colors.get("reset", 0)))

def error(message):
    print("%s%s%s" % (colors.get("red", 1), message, colors.get("reset", 0)))

def loading(message):
    print("%s%s%s" % (colors.get("cyan", 0), message, colors.get("reset", 0)))

def result(name, logo, color):
    print("%s  | %s%s%s %s" % (
        time.get(), 
        colors.get(f"{color}", 1),
        logo,
        colors.get("reset", 0),
        name))