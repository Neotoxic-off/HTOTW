import json

def code(result):
    if (result.status_code == 200):
        return (1)
    return (-1)

def data(message, result):
    return (1)

def check(method, message, result):
    if (method == "code"):
        return (code(result))

    if (method == "data"):
        return (data(message, result))
    print(f"No verification method for '{method}'")
    return (-1)
