import json
import datetime

from src import loaders
from src import colors
from src import banner
from src import logs
from src import requester

class search_settings:
    adult = None

class search_result:
    founded = 0
    dead = 0

class HTOTW_RESULT:
    def code(self, result, name, settings):
        success_code = name["error"]["status_code"]["ok"]

        if (result.status_code == settings.configuration["status_code"][success_code]):
            return (1)
        return (0)

    def data(self, message, result):
        return (1)

    def check(self, method, message, result, name, settings):
        if (method == "status_code"):
            return (self.code(result, name, settings))
        if (method == "text"):
            return (self.data(message, result))
        if (method):
            logs.error(
                settings.configuration["HTOTW_RESULT"]
                ["verification"]
                ["method"]
                ["unknown"]
                .replace("{}", name["name"])
                .replace("[]", method)
            )
            return (-1)
    
    def resume(self, settings, username):
        founded = "%d" % search_result.founded

        logs.action(settings.configuration["HTOTW_ENGINE"]
            ["hunt"]
            ["end"]
        )
        logs.resume(settings.configuration["HTOTW_RESULT"]
            ["resume"]
            ["found"]
            .replace("{}", username)
            .replace("[]", founded)
        )

class HTOTW_ENGINE:
    def display(self, special, name, logo, color):
        logs.result(special = special, name = name, logo = logo, color = color)
    
    def check(self, special, name, verification, settings):
        if (verification == 1):
            self.display(special = special, name = name, logo = settings.settings["status"]["ok"], color = "green")
            search_result.founded += 1
        elif (verification == 0):
            self.display(special = special, name = name, logo = settings.settings["status"]["error"], color = "red")

    def adult(self, host, settings):
        if (host["adult"] == True):
            if (settings.adult == True):
                return (1)
            return (-1)
        return (0)
    
    def group(self, i, total):    
        if (total > 1):
            if (i == 0):
                return ('┌')
            elif (i == total - 1):
                return ('└')
            else:
                return ('│')
        return ('')

    def search(self, name, settings, username, htotw_result):
        urls = len(name["url"])
        special = None

        for i in range(urls):
            special = self.group(i, urls)
            request_url = "%s" % name["url"][i].replace("{}", username)
            result = requester.do_request(name["error"]["method"], name["method"], name["header"], request_url)
            verification = htotw_result.check(
                method = name["error"]["method"],
                message = name["error"]["message"],
                result = result,
                name = name,
                settings = settings
            )   
            self.check(
                special = special,
                name = name["name"],
                verification = verification,
                settings = settings
            )
    
    def count_links(self, modules):
        total = 0

        for host in modules.keys():
            count = len(modules[host]["url"])
            for i in range(count):
                total += 1
        
        return (total)

    def run(self, modules, settings, username):
        htotw_result = HTOTW_RESULT()
        hosts = "%d" % len(modules.keys())
        links = "%d" % self.count_links(modules = modules)

        logs.log(settings.configuration["HTOTW_ENGINE"]
            ["total_hosts"]
            .replace("{}", hosts)
        )
        logs.log(settings.configuration["HTOTW_ENGINE"]
            ["total_links"]
            .replace("{}", links)
        )
        logs.action(settings.configuration["HTOTW_ENGINE"]
            ["hunt"]
            ["start"]
        )

        for host in modules.keys():
            if (self.adult(host = modules[host], settings = settings) != -1):
                self.search(
                    name = modules[host],
                    settings = settings,
                    username = username,
                    htotw_result = htotw_result
                )

        htotw_result.resume(settings = settings, username = username)
