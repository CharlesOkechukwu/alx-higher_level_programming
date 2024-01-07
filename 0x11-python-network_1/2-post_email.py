#!/usr/bin/python3
"""send a post request to a url link"""
from sys import argv
import urllib.request
import urllib.parse


if __name__ == "__main__":
    value = {'email': argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    url = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(url) as response:
        response = response.read()
        print(response.decode('utf-8'))
