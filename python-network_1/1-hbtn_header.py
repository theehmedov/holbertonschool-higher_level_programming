#!/usr/bin/python3
"""Fetches the X-Request-Id header value from a given URL"""
from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with request.urlopen(url) as response:
        x_request_id = response.getheader("X-Request-Id")
        print(x_request_id)
