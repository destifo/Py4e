#this program returns the last element of a list that contains the content of an anchor tag
# at position POS after following the links COUNT number of times
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter the url - ")
count = int(input("Enter the count: "))
pos = int(input("Enter the position: "))

namelst = list()

def link_follower(url, count, pos):
    try:
        if count == 0:
            return namelst[-1]
    except:
        if pos > 3:
            return "Index out of Bound"
        return "Nothing was accessed from the site"
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    html = tags[pos-1].get('href', None)
    namelst.append(tags[pos-1].contents[0])
    return link_follower(html, count - 1, pos)


print(link_follower(url, count, pos))
