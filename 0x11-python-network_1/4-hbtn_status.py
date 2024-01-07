#!/usr/bin/python3
"""module to fetch resource from a url"""
import requests

if __name__ == "__main__":
    """import and print out
    the resource"""
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
