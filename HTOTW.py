#!/usr/bin/env python3

import json
import argparse

from src import engine

from src import loaders
from src import colors
from src import banner
from src import logs
from src import requester

class search_settings:
    adult = None
    settings = None
    username = None
    configuration = None

class modules:
    content = None

class searches:
    ok = 0
    error = 0


class HTOTW_LOAD:
    def settings():
        logs.loading("loading settings...")
        search_settings.settings = loaders.settings()

    def configuration():
        logs.loading("loading configuration...")
        search_settings.settings = loaders.configuration()

    def modules():
        logs.loading("loading modules...")
        modules.content = loaders.modules()
    
    def engine():
        logs.loading("loading engine...")
        return (engine.HTOTW_ENGINE())

def arguments():
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description = "All commands availables")
    required_settings = parser.add_argument_group("Required settings")
    required_settings.add_argument("-u", "--username", action = "store",   help = "Username to hunt", required = True)
    parser.add_argument("-a", "--adult", action = "store_true", help = "Check the adult hosts", default = False)
    args = parser.parse_args()
    search_settings.adult = args.adult
    search_settings.username = args.username

def header():
    banner.load()
    banner.display()

def main():
    load = HTOTW_LOAD
    arguments()
    header()
    load.settings()
    load.modules()
    engine_access = load.engine()
    engine_access.run(modules = modules.content, settings = search_settings, username = search_settings.username)

if (__name__ == "__main__"):
    main()