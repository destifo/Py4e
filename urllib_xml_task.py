import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def xml_url_in():
    url = input("Enter your url: ")
    temp = url.lower().split('.')
    if 'xml' not in temp:
        print("The html doesn't have an xml file in it.")
        print("Please enter valid url again")
        return xml_url_in()
    return url

def url_reader(url):
    return urllib.request.urlopen(url, context=ctx).read()

def xml_parser(xml):
    element = ET.fromstring(xml)
    comment_list = element.findall('comments/comment')
    count_list = list()
    for item in comment_list:
        count_list.append(int(item.find('count').text))
    #print(count_list)
    return sum(count_list)

url = xml_url_in()
xml = url_reader(url)
print(xml_parser(xml))
