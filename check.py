import sys
import urllib.request
import json
import time
url1 = "http://tile38-write:9851/server"
url2 = "http://0.0.0.0:9851/server"

master_not_ready = True
self_not_ready = True

def make_request(url):
    res = urllib.request.urlopen(url)
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
    except:
        wait()

while self_not_ready:
    try:
        obj = make_request(url2)
        if obj['stats']['num_objects'] > 10:
            self_not_ready = False
            break
    except:
        wait()

