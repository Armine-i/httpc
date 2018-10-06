#!/usr/bin/env python3

import socket
import json
import pprint
from http_parser.http import HttpStream
from http_parser.reader import SocketReader

PORT = 80
#header syntax for GET request
#                        ----URL----             -------URL-------    -----header------
request_headerGET = 'GET /get?course=networking&assignment=1 HTTP/1.0\r\nHost: httpbin.org\r\nConnection: close\r\n\r\n'

#header syntax for POST request
data=json.dumps({"c": 0, "b": 0, "a": 0})
#                          -URL-             -------URL-------    -----------------------------------------header------------------------------------------        -d or -f
request_headerPOST = 'POST /post HTTP/1.0\r\nHost: httpbin.org\r\nContent-Type:application/json\r\nContent-Length: '+str(len(data))+'\r\nConnection: close\r\n\r\n'+data+'\r\n\r\n'

def POSTverbose(HOST, request_headerPOST):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        try:
            s.sendall(request_headerPOST.encode('utf-8'))
        except:
            print("An error has occured while trying to send the POST request")
        dataReceived = SocketReader(s)
        parsed = HttpStream(dataReceived)
        body = parsed.body_file().read().decode('utf-8')
        header = parsed.headers()
        return pprint.pformat(header) + body

def recPOSTbody(HOST, request_headerPOST):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        try:
            s.sendall(request_headerPOST.encode('utf-8'))
        except:
            print("An error has occured while trying to send the POST request")
        dataReceived = SocketReader(s)
        parsed = HttpStream(dataReceived)
        body = parsed.body_file().read().decode('utf-8')
        return body

def recPOSTheader(HOST, request_headerPOST):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        try:
            s.sendall(request_headerPOST.encode('utf-8'))
        except:
            print("An error has occured while trying to send the POST request")
        dataReceived = SocketReader(s)
        parsed = HttpStream(dataReceived)
        header = parsed.headers()
        return header

def GETverbose(HOST, request_headerGET):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, 80))
        try:
            s.sendall(request_headerGET.encode('utf-8'))
        except:
            print("An error has occured while trying to send the GET request")
        dataReceived = SocketReader(s)
        parsed = HttpStream(dataReceived)
        body = parsed.body_file().read().decode('utf-8')
        header = parsed.headers()
        return pprint.pformat(header) + body

def recGETbody(HOST, request_headerGET):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        try:
            s.sendall(request_headerGET.encode('utf-8'))
        except:
            print("An error has occured while trying to send the GET request")
        dataReceived = SocketReader(s)
        parsed = HttpStream(dataReceived)
        body = parsed.body_file().read().decode('utf-8')
        return body

def recGETheader(HOST, request_headerGET):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        try:
            s.sendall(request_headerGET.encode('utf-8'))
        except:
            print("An error has occured while trying to send the GET request")
        dataReceived = SocketReader(s)
        parsed = HttpStream(dataReceived)
        header = parsed.headers()
        return header

#print(recGETbody("httpbin.org", request_headerGET))
#print(POSTverbose())