#!/usr/bin/python3
"""send request to a url and print the response"""
from sys import argv
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(url) as response:
            response = response.read()
            print(response.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
