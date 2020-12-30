#!/usr/bin/env python3

import json
import requests
import argparse

from src import loaders
from src import verify
from src import colors
from src import banner
from src import logs

class settings:
    adult = None
    settings = None
    hosts = None
    username = None
    configuration = None

class host:
    settings = None

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

def do_request(method, headers, url):
    if (method == "GET"):
        return (requests.get(url, headers = headers))
    if (method == "PUT"):
        return (requests.put(url, headers = headers))
    return (requests.post(url, headers = headers))

def search(count, name, user):
    result = do_request(host.settings["method"], host.settings["header"], ("%s%s" % (host.settings["url"], user)))
    verification = verify.check(host.settings["error"]["method"], host.settings["error"]["message"], result)

    if (verification == 1):
        logs.result_used(count, name, settings.settings["status"]["ok"])
    else:
        logs.result_free(count, name, settings.settings["status"]["error"])

def engine(user):
    total = len(settings.hosts)

    logs.action("Starting the hunt...\n")
    for i in range(total):
        load_host_configuration(f"modules/{settings.hosts[i]}")
        if (host.settings["adult"] == 1):
            if (settings.adult == True):
                search(f"[{i + 1}/{total}]", settings.hosts[i], user)
        else:
            search(f"[{i + 1}/{total}]", settings.hosts[i], user)            

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
    load_hosts()
    engine(settings.username)

main()