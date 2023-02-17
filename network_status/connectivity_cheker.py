import urllib.request


class ConnectivityChecker:
    def __init__(self):
        self.host = 'http://google.com'

    def check_connection(self):
        try:
            urllib.request.urlopen(self.host)
            return True
        except:
            return False

