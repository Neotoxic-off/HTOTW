import os
import json

def settings():
    with open("settings/settings.json", 'r') as f:
        data = json.load(f)
    return (data)

def configuration():
    with open("settings/configuration.json", 'r') as f:
        data = json.load(f)
    return (data)

def hosts():
    return (os.listdir("modules"))

def host_configuration(module):
    with open(module, 'r') as f:
        data = json.load(f)
    return (data)