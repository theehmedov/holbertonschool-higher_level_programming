#!/usr/bin/python3
"""Sends a POST request with an email parameter using requests"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # POST datası
    data = {'email': email}

    # POST sorğusu göndəririk
    response = requests.post(url, data=data)

    # Cavabı ekrana çıxarırıq
    print(response.text)
