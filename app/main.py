activate_this = '/Users/likit/.virtualenvs/biolytics/bin/activate_this.py'
exec(open(activate_this).read(), dict(__file__=activate_this))

from time import sleep
from threading import Thread

import webview
from server import run_server

def url_ok(url, port):
    try:
        from http.client import HTTPConnection
    except ImportError:
        from httplib import HTTPConnection

    try:
        conn = HTTPConnection(url, port)
        conn.request("GET", "/")
        r = conn.getresponse()
        return r.status == 200
    except:
        return False


if __name__ == '__main__':
    t = Thread(target=run_server)
    t.daemon = True
    t.start()

    while not url_ok("127.0.0.1", 5000):
        sleep(0.1)


    webview.create_window("Biolytics", "http://127.0.0.1:5000",
        resizable=True, width=1024, height=800, confirm_quit=True)