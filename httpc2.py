#!/usr/bin/env python3

import click
import echoclient as lib
import re

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
    click.echo(url)
    path = "/".join(re.findall(r'[^/]+', url)[+2:])
    host = url.split("//")[-1].split("/")[0].split('?')[0]
    final = "GET " + path + " HTTP/1.0\r\nHost: " + host + "\r\n" + h + "\r\n\r\n"
    if v:
        click.echo(lib.GETverbose(host, final))
    else:
        click.echo(lib.recGETbody(host, final))

@cli.command(help="Post executes a HTTP POST request for a given URL with inline data or from file.")
@click.option('-v', is_flag=True, help="Prints the detail of the response such as protocol, status, and headers.")
@click.option('-h', is_flag=True, multiple=True, help="Associates headers to HTTP Request with the format 'key:value'.")
@click.option('-d', 'data', flag_value='d', help="Associates an inline data to the body HTTP POST request.")
@click.option('-f', 'data', flag_value='f', help="Associates the content of a file to the body HTTP POST request.")
@click.argument('URL', nargs=1)
def post():
    click.echo('Dropped the database')