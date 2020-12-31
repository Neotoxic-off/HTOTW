import json
import datetime

from src import loaders
from src import colors
from src import banner
from src import logs
from src import requester

class search_settings:
    adult = None

class HTOTW_RESULT:
    def code(self, result, name, settings):
        success_code = name["error"]["code"]["ok"]

        if (result.status_code == settings.configuration["status_code"][success_code]):
            return (1)
        return (-1)

    def data(self, message, result):
        return (1)

    def check(self, method, message, result, name, settings):
        if (method == "code"):
            return (self.code(result, name, settings))
        if (method == "data"):
            return (self.data(message, result))

        logs.error(f"No verification method for '{method}'")

        return (-1)

class HTOTW_ENGINE:
    def display(self, name, logo, color):
        logs.result(name = name, logo = logo, color = color)
    
    def check(self, name, verification, settings):
        if (verification == 1):
            self.display(name = name, logo = settings.settings["status"]["ok"], color = "green")
        else:
            self.display(name = name, logo = settings.settings["status"]["error"], color = "red")

    def adult(self, host, settings):
        if (host["adult"] == True):
            if (settings.adult == True):
                return (1)
            return (-1)
        return (0)

    def search(self, name, settings, username):
        htotw_result = HTOTW_RESULT()
        url = "%s" % name["url"].replace("{}", username)
        result = requester.do_request(name["error"]["method"], name["method"], name["header"], url)
        verification = htotw_result.check(
            method = name["error"]["method"],
            message = name["error"]["message"],
            result = result,
            name = name,
            settings = settings
        )

        self.check(
            name = name["name"],
            verification = verification,
            settings = settings
        )

    def run(self, modules, settings, username):
        logs.log("Total websites: %d" % len(modules.keys()))
        logs.action("starting the hunt...")

        for host in modules.keys():
            if (self.adult(host = modules[host], settings = settings) != -1):
                self.search(name = modules[host], settings = settings, username = username)
