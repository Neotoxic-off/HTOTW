import requests

def do_request(e_method, method, headers, url):
    if (e_method == "code"):
        return (requests.head(url, headers = headers))
    if (method == "GET"):
        return (requests.get(url, headers = headers))
    if (method == "POST"):
        return (session.post(url, headers = headers))
    return (requests.put(url, headers = headers))