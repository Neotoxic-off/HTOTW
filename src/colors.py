def get(c, f):
    data = {
        "reset"  : "0",
        "red"    : "31",
        "green"  : "32",
        "yellow" : "33",
        "blue"   : "34",
        "purple" : "35",
        "cyan"   : "36",
        "white"  : "37"
    }
    if data.get("%s" % c) != None and (f >= 0 and f <= 5):
        return ("\033[%s;%sm" % (f, data.get("%s" % c)))
    return (None)