import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'



api_url = 'http://py4e-data.dr-chuck.net/json?'

while True:
    address = input("Enter an address: ")
    if len(address) < 1:
        print("No address")
        break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = api_url + urllib.parse.urlencode(parms)
    print("Retrieving:", url)

    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    print("Retrieved", len(data), "characters")

    #print(data)
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js["status"] != 'OK':
        print("==== Failed to retrieve the data ====")
        print(data)
        continue
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    location = js["results"][0]["formatted_address"]
    print('Place id:', js["results"][0]["place_id"])
    print('location:', location)
