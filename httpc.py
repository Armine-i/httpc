import argparse

parser = argparse.ArgumentParser()
parser.parse_args()
subparsers = parser.add_subparsers()

# create the parser for the "get" command
parser_get = subparsers.add_parser('get', help='Get executes a HTTP GET request for a given URL.')
parser_get.add_argument('url')
argsget = parser_get.parse_args()
print(argsget.url)

# create the parser for the "post" command
parser_post = subparsers.add_parser('post', help='Post executes a HTTP POST request for a given URL with inline data or from file.')
argspost = parser_post.parse_args()
parser_post.add_argument('url')


