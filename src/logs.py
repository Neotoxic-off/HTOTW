from src import colors

def action(message):
    print("%s%s%s" % (colors.get("blue", 1), message, colors.get("reset", 0)))

def load(message):
    print("%s%s%s" % (colors.get("cyan", 1), message, colors.get("reset", 0)))

def result_free(count, name, logo):
    print("%s%s%s %s%s%s %s" % (
        colors.get("yellow", 1),
        count,
        colors.get("reset", 0),
        colors.get("red", 1),
        logo,
        colors.get("reset", 0),
        name))

def result_used(count, name, logo):
    print("%s%s%s %s%s%s %s" % (
        colors.get("yellow", 1),
        count,
        colors.get("reset", 0),
        colors.get("green", 1),
        logo,
        colors.get("reset", 0),
        name))
