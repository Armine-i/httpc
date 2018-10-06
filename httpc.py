#!/usr/bin/env python3

import click
import echoclient as lib
import re
import json

#httpc post [-v] [-h key:value] [-d inline-data] [-f file] URL
#httpc get [-v] [-h key:value] URL

requestGET = 'GET /status/418 HTTP/1.0\r\nHost: httpbin.org\r\nConnection: close\r\n\r\n'

@click.group()
def cli():
    pass

@cli.command(help="Get executes a HTTP GET request for a given URL.")
@click.argument('url', type=str)
@click.option('-v', is_flag=True, type=str, help="Prints the detail of the response such as protocol, status, and headers.")
@click.option('-h', nargs=1, default="Connection:close", type=str, help="Associates headers to HTTP Request with the format 'key:value'.")
def get(url, v, h):
    path = "/".join(re.findall(r'[^/]+', url)[+2:])
    host = url.split("//")[-1].split("/")[0].split('?')[0]
    final = "GET " + path + " HTTP/1.0\r\nHost: " + host + "\r\n" + h + "\r\n\r\n"
    if v:
        click.echo(lib.GETverbose(host, final))
    else:
        click.echo(lib.recGETbody(host, final))

@cli.command(help="Post executes a HTTP POST request for a given URL with inline data or from file.")
@click.option('-v', is_flag=True, help="Prints the detail of the response such as protocol, status, and headers.")
@click.option('-h', nargs=1, default="Content-Type:application/json", type=str, help="Associates headers to HTTP Request with the format 'key:value'.")
@click.option('--d', multiple=True, type=str, help="Associates an inline data to the body HTTP POST request.")
@click.argument('url', type=str)
def post(v, h, d, url):
    path = "/".join(re.findall(r'[^/]+', url)[+2:])
    host = url.split("//")[-1].split("/")[0].split('?')[0]
    data = json.dumps(d)
    length = str(len(data))
    final = 'POST /' + path + ' HTTP/1.0\r\nHost: ' + host + '\r\n' + h + '\r\nContent-Length: ' +length+ '\r\nConnection: close\r\n\r\n'+data+'\r\n\r\n'
    if v:
        click.echo(lib.POSTverbose(host, final))
    else:
        click.echo(lib.recPOSTbody(host, final))
