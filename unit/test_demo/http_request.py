import requests


class HttpRequest:
    """"利用requests
    """

    def http_request(self, url, data, method, cookie=None):
        if method.lower() == 'get':
            res = requests.get(url, data, cookies=cookie, verify=False)
        else:
            res = requests.post(url, data, cookies=cookie, verify=False)
        return res


if __name__ == '__main__':
    pass
