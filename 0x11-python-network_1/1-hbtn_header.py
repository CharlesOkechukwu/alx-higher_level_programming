#!/usr/bin/python3
"""send request to a url and display the request id"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    url = urllib.request.Request(argv[1])
    with urllib.request.urlopen(url) as response:
        header = response.info()
        print(header.get('X-Request-Id'))
