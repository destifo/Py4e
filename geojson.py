import urllib.request, urllib.parse, urllib.parse
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
    address = input("Enter your location: ")
    if len(address) < 1: break
    url = serviceurl + urllib.parse.urlencode({"address": address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js["status"] != 'OK':
        print('==== Failed to retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print("latitude:", lat, "longitude:", lng)
    location = js["results"][0]["formatted_address"]
    print("location:", location)
