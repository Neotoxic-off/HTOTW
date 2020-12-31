from src import colors
from src import time

def action(message):
    print("%s  | %s%s%s" % (
        time.get(), 
        colors.get("blue", 0),
        message,
        colors.get("reset", 0)))

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

def result(name, logo, color):
    print("%s  | %s%s %s%s" % (
        time.get(), 
        colors.get(color, 0),
        logo,
        name,
        colors.get("reset", 0)))