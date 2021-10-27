import json
import ssl
import sqlite3 as sq
import urllib.request, urllib.error, urllib.parse
import http
import sys
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = False

if api_key is False:
    api_key = 42
    api_url = 'http://py4e-data.dr-chuck.net/json?'
else:
    api_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

conn = sq.connect('databases/geodatadb.sqlite')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS Location(address TEXT, geodata TEXT);
''')
fname = input('Enter the file name: ')
if len(fname) < 1: fname = 'where.data'
fh = open(fname)
address_count = 0
for line in fh:
    if address_count > 200:
        print('REtrieved 200 locations, Restart to retrieve more...')
        break
    address = line.strip()
    print('')
    cur.execute('SELECT geodata FROM Location WHERE address = ?', (memoryview(address.encode()),))

    try:
        data = cur.fetchone()[0]
        print('Found in the database', address)
        continue
    except:
        pass

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = api_url + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context = ctx).read()
    data = connection.decode()
    print('Retrieved', len(data), 'characters')

    try:
        js_data = json.loads(data)
    except:
        print('====Failed to retrieve data====')
        print(data)
        continue
    if not js_data or 'status' not in js_data or js_data["status"] != 'OK':
        print("**** Failed to retrieve the data ****")
        print(data)
        break

    cur.execute('''INSERT INTO Location(address, geodata)
        VALUES (?, ?)''', (memoryview(address.encode()), memoryview(data.encode())))

    conn.commit()

    if address_count % 10 == 0:
        print('pausing for 5 seconds...')
        time.sleep(5)
    print("Press Ctrl + C to terminate the process")
