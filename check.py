import sys
import httplib
import json
import time
url1 = "tile38-write"
url2 = "127.0.0.1"
port = 9851

master_not_ready = True
self_not_ready = True

def make_request(url):
    conn = httplib.HTTPConnection(url, port)
    conn.request("GET", "/server")
    res = conn.getresponse()
    body = res.read().decode('utf-8')
    return json.loads(body)

def wait():
    sys.stdout.write('.')
    sys.stdout.flush()
    time.sleep(1)
    return

while master_not_ready:
    try:
        obj = make_request(url1)
        if obj['stats']['num_objects'] > 10:
            master_not_ready = False
            break
    except Exception as err:
        # print(err)
        wait()

while self_not_ready:
    try:
        obj = make_request(url2)
        if obj['stats']['num_objects'] > 10:
            self_not_ready = False
            break
    except Exception as err:
        # print(err)
        wait()

