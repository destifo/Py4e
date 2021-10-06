import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print("This program extracts data from a web server using url provided")
url = input("Enter the url: ")
connection = urllib.request.urlopen(url, context=ctx)
data = connection.read().decode()

js = json.loads(data)
comments_count_list = list()
for comment in js["comments"]:
    comments_count_list.append(comment["count"])
print(sum(comments_count_list))
