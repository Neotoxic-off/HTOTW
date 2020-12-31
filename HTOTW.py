#!/usr/bin/env python3

import json
import argparse
import datetime

from src import loaders
from src import verify
from src import colors
from src import banner
from src import logs
from src import requester

class settings:
    adult = None
    settings = None
    username = None
    configuration = None

class modules:
    content = None

class searches:
    ok = 0
    error = 0

def time():
    return ("%s%s%s" % (colors.get("green", 3), datetime.datetime.now().strftime("%H:%M:%S"), colors.get("reset", 0)))

def load_settings():
    logs.load("loading settings...")
    settings.settings = loaders.settings()

def load_configuration():
    logs.load("loading configuration...")
    settings.settings = loaders.configuration()

def load_modules():
    logs.load("loading modules...")
    modules.content = loaders.modules()

def search(name, user):
    url = "%s" % name["url"].replace("{}", user)
    result = requester.do_request(name["error"]["method"], name["method"], name["header"], url)
    verification = verify.check(name["error"]["method"], name["error"]["message"], result)

    if (verification == 1):
        logs.result_used("%s  | " % time(), name["name"], settings.settings["status"]["ok"])
        searches.ok += 1
    else:
        logs.result_free("%s  | " % time(), name["name"], settings.settings["status"]["error"])
        searches.error += 1

def engine(user):
    logs.action("\nSTARTING THE HUNT...\n")

    for host in modules.content.keys():
        if (modules.content[host]["adult"] == 1):
            if (settings.adult == True):
                search(modules.content[host], user)
        else:
            search(modules.content[host], user)
    if (searches.ok > 1):
        char = 's'
    else:
        char = ''
    print(f"\n{user} founded on {searches.ok} website{char}")

def arguments():
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description = "All commands availables")
    required_settings = parser.add_argument_group("Required settings")
    required_settings.add_argument("-u", "--username", action = "store",   help = "Username to hunt", required = True)
    parser.add_argument("-a", "--adult", action = "store_true", help = "Check the adult hosts", default = False)
    args = parser.parse_args()
    settings.adult = args.adult
    settings.username = args.username

def header():
    banner.load()
    banner.display()

def main():
    arguments()
    header()
    load_settings()
    load_modules()
    engine(settings.username)

if (__name__ == "__main__"):
    main()