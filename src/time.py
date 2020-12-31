import datetime

from src import colors

def get():
    return ("%s%s%s" % (colors.get("green", 3), datetime.datetime.now().strftime("%H:%M:%S"), colors.get("reset", 0)))
