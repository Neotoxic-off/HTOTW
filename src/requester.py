from requests_futures.sessions import FuturesSession

def do_request(e_method, method, headers, url):
    session = FuturesSession(max_workers = 20)

    if (e_method == "code"):
        request_head = session.head(url, headers = headers)
        result = request_head.result()
        return (result)
    if (method == "GET"):
        request_get = session.get(url, headers = headers)
        result = request_get.result()
        return (result)
    if (method == "POST"):
        request_post = session.post(url, headers = headers)
        result = request_post.result()
        return (result)
    request_put = session.put(url, headers = headers)
    result = request_put.result()
    return (result)