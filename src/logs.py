from src import colors
from src import time

def action(message):
    print("\n%s  | %s%s%s" % (
        time.get(), 
        colors.get("blue", 0),
        message,
        colors.get("reset", 0)), end = "\n\n")

def resume(message):
    print("%s%s%s" % (
        colors.get("purple", 0),
        message,
        colors.get("reset", 0)), end = "\n")

def error(message):
    print("%s  | %s%s%s" % (
        time.get(), 
        colors.get("red", 0),
        message,
        colors.get("reset", 0)))

def loading(message):
    print("%s  | %sloading %s...%s" % (
        time.get(), 
        colors.get("cyan", 0),
        message,
        colors.get("reset", 0)))

def log(message):
    print("%s  | %s%s%s" % (
        time.get(), 
        colors.get("purple", 0),
        message,
        colors.get("reset", 0)))

def result(special, modules, logo, color):
    print("%s  | %s%s %s%s%s %s%s" % (
        time.get(),
        colors.get(color, 0),
        logo,
        colors.get("reset", 0),
        special,
        colors.get(color, 0),
        modules,
        colors.get("reset", 0)))
    
def timeout(special, modules, logo):
    print("%s  | %s⌚ %s%s%s %s%s" % (
        time.get(),
        colors.get("orange", 0),
        logo,
        colors.get("reset", 0),
        special,
        colors.get("orange", 0),
        modules,
        colors.get("reset", 0)))

def down(modules, logo, color):
    print("%s  | %s%s %s%s%s" % (
        time.get(),
        colors.get(color, 0),
        logo,
        colors.get(color, 0),
        modules,
        colors.get("reset", 0)))