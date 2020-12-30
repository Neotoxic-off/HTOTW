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
    hosts = None
    username = None
    configuration = None
    output = None

class host:
    settings = None

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

def load_hosts():
    logs.load("loading hosts...")
    settings.hosts = loaders.hosts()

def load_host_configuration(module):
    host.settings = loaders.host_configuration(module)

def search(name, user):
    url = "%s" % host.settings["url"].replace("{}", user)
    result = requester.do_request(host.settings["error"]["method"], host.settings["method"], host.settings["header"], url)
    verification = verify.check(host.settings["error"]["method"], host.settings["error"]["message"], result)

    if (verification == 1):
        logs.result_used("%s  | " % time(), name, settings.settings["status"]["ok"])
        searches.ok += 1
    else:
        logs.result_free("%s  | " % time(), name, settings.settings["status"]["error"])
        searches.error += 1

    if (settings.output != None):
        f = open(settings.output, "a")
        f.write(f"{url}\n")
        f.close()

def engine(user):
    total = len(settings.hosts)
    logs.action("Running the hunt...\n")

    for i in range(total):
        load_host_configuration(f"modules/{settings.hosts[i]}")
        if (host.settings["adult"] == 1):
            if (settings.adult == True):
                search(settings.hosts[i], user)
        else:
            search(settings.hosts[i], user)
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
    parser.add_argument("-o", "--output", action = "store", help = "Name of the ouput file", default = None)
    args = parser.parse_args()
    settings.adult = args.adult
    settings.username = args.username
    settings.output = args.output

def header():
    banner.load()
    banner.display()

def main():
    arguments()
    header()
    load_settings()
    load_hosts()
    engine(settings.username)

if (__name__ == "__main__"):
    main()