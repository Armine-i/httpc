import argparse

parser = argparse.ArgumentParser()
parser.description = "Get executes a HTTP GET request for a given URL."
parser.add_argument("url")
parser.parse_args()

