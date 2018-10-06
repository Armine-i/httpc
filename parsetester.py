import urllib.parse
import echoclient as lib
import re

request_headerGET = 'GET /status/418 HTTP/1.0\r\nHost: httpbin.org\r\nConnection: close\r\n\r\n'

user = "get -v 'http://httpbin.org/get?course=networking&assignment=1 -h Connection:close"

user = user.replace('http://', ' ')


URL = "http://httpbin.org/get?course=networking&assignment=1"
host = URL.split("//")[-1].split("/")[0].split('?')[0]

h = "Connection:close"
path = "/".join(re.findall(r'[^/]+', URL)[+2:])
path1 = urllib.parse.urlparse(URL).path
path2 = urllib.parse.urlparse(URL).query
finalPath = path1 + "?" + path2
print(path)
#final = "GET " + path + " HTTP/1.0\r\nHost: " + host + "\r\n" + h + "\r\n\r\n"

#print(final)

#print(lib.recGETbody("httpbin.org", final))