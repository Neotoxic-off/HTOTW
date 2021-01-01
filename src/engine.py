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
    down = 0

class HTOTW_DOWN:
    def display(self, modules, logo, color):
        logs.down(modules = modules, logo = logo, color = color)
    
    def adult(self, host, settings):
        if (host["adult"] == True):
            if (settings.adult == True):
                return (1)
            return (-1)
        return (0)

    def down(self, modules, settings):
        for host in modules.keys():
            if (self.adult(host = modules[host], settings = settings) != -1):
                if (self.check(
                        url = modules[host]["origin"],
                        modules = modules[host],
                        settings = settings
                    ) == 1):
                    self.display(
                        modules = modules[host]["name"],
                        logo = settings.settings["down"]["ok"],
                        color = "green"
                    )
                else:
                    self.display(
                        modules = modules[host]["name"],
                        logo = settings.settings["down"]["error"],
                        color = "red"
                    )
                    search_result.down += 1

    def check(self, url, modules, settings):
        result = requester.do_request("GET", "status_code", modules["header"], url, modules["timeout"])
        if (result != -1):
            if (result.status_code == settings.configuration["status_code"]
                    [modules["error"]["status_code"]["default"]]
                    or
                    result.status_code != settings.configuration["status_code"]
                    ["not_found"]
                    or result.text
                ):
                    return (1)
        return (-1)
    
    def resume(self, settings):
        down = "%d" % search_result.down

        logs.action(settings.configuration["HTOTW_ENGINE"]
            ["down"]
            ["end"]
        )
        logs.resume(settings.configuration["HTOTW_RESULT"]
            ["resume"]
            ["down"]
            .replace("{}", down)
        )

class HTOTW_RESULT:
    def code(self, result, modules, settings):
        success_code = modules["error"]["status_code"]["ok"]

        if (result.status_code == settings.configuration["status_code"][success_code]):
            return (1)
        return (0)

    def data(self, message, result):
        return (1)

    def check(self, method, message, result, modules, settings):
        if (method == "status_code"):
            return (self.code(result, modules, settings))
        if (method == "text"):
            return (self.data(message, result))
        if (method):
            logs.error(
                settings.configuration["HTOTW_RESULT"]
                ["verification"]
                ["method"]
                ["unknown"]
                .replace("{}", modules["name"])
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
    def display(self, special, modules, logo, color):
        logs.result(special = special, modules = modules, logo = logo, color = color)
    
    def check(self, special, modules, verification, settings):
        if (verification == 1):
            self.display(special = special, modules = modules, logo = settings.settings["status"]["ok"], color = "green")
            search_result.founded += 1
        elif (verification == 0):
            self.display(special = special, modules = modules, logo = settings.settings["status"]["error"], color = "red")

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

    def search(self, modules, settings, username, htotw_result):
        urls = len(modules["url"])
        special = None

        for i in range(urls):
            special = self.group(i, urls)
            request_url = "%s" % modules["url"][i].replace("{}", username)
            result = requester.do_request(modules["error"]["method"], modules["method"], modules["header"], request_url, modules["timeout"])
            if (result != -1):
                verification = htotw_result.check(
                    method = modules["error"]["method"],
                    message = modules["error"]["message"],
                    result = result,
                    modules = modules,
                    settings = settings
                )   
                self.check(
                    special = special,
                    modules = modules["name"],
                    verification = verification,
                    settings = settings
                )
            else:
                self.check(
                    special = special,
                    modules = modules["name"],
                    verification = 0,
                    settings = settings
                )
    
    def count_links(self, modules):
        total = 0

        for host in modules.keys():
            count = len(modules[host]["url"])
            for i in range(count):
                total += 1
        
        return (total)
    
    def down(self, modules, settings):
        htotw_down = HTOTW_DOWN()

        logs.action(settings.configuration["HTOTW_ENGINE"]
            ["down"]
            ["start"]
        )
        htotw_down.down(modules = modules, settings = settings)
        htotw_down.resume(settings = settings)

    def engine(self, modules, settings, username):
        htotw_result = HTOTW_RESULT()

        logs.action(settings.configuration["HTOTW_ENGINE"]
            ["hunt"]
            ["start"]
        )
        for host in modules.keys():
            if (self.adult(host = modules[host], settings = settings) != -1):
                self.search(
                    modules = modules[host],
                    settings = settings,
                    username = username,
                    htotw_result = htotw_result
                )
        htotw_result.resume(settings = settings, username = username)

    def run(self, modules, settings, username):
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
        if (settings.status == True):
            self.down(modules = modules, settings = settings)
        self.engine(
            modules = modules,
            settings = settings,
            username = username
        )