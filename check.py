import sys
import urllib.request
import json
import time
url = "http://tile38-write:9851/server"
# url = "http://localhost:9851/server"

not_ready = True

while not_ready:
    try:
        res = urllib.request.urlopen(url)
        body = res.read().decode('utf-8')
        obj = json.loads(body)
        if obj['stats']['num_objects'] > 10:
            not_ready = False
            break
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)
    except:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)
