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

class HTOTW_LOAD:
    def settings():
        try:
            search_settings.settings = loaders.settings()
            logs.loading("loading settings...")
        except Exception:
            logs.error("loading settings...")

    def configuration():
        try:
            search_settings.settings = loaders.configuration()
            logs.loading("loading configuration...")
        except Exception:
            logs.error("loading configuration...")

    def modules():
        try:
            modules.content = loaders.modules()
            logs.loading("loading modules...")
        except Exception:
            logs.error("loading modules...")
    
    def engine():
        try:
            access = engine.HTOTW_ENGINE()
            if (access):
                logs.loading("loading engine...")
                return (access)
            else:
                logs.error("loading engine...")
        except Exception:
            logs.error("loading engine...")

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