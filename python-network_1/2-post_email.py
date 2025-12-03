#!/usr/bin/python3
"""Sends a POST request with an email parameter to a given URL"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Email parametrini POST datasına çeviririk
    data = parse.urlencode({'email': email}).encode('utf-8')

    # Request obyektini yaradırıq
    req = request.Request(url, data=data, method='POST')

    # Sorğunu göndəririk
    with request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
