import urllib.request, urllib.parse, urllib.error
import json
import ssl
import twurl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

twitter_url = ''

while True:
    account = input("Enter an account: ")
    if len(account) < 1: break
    url = twurl.augment(twitter_url, {'screen_name': account, 'count': '2'})
    connection = urllib.request.urlopen(url, context=ctx)
    print(Retrieving, url)
    data = connection.read().decode()
    print(json.dumps(data, indent=4))

    headers = dict(connection.getheaders())
    print('Remaining tries:', headers['x-rate-limit-remaining'])

    js = json.loads(data)
    for u in js[users]:
        print('Name:', u["screen_name"])
        if 'status' not in u:
            print("No status found for this person")
            continue
        status = u["status"]["text"]
        print('status:', status[:80])
