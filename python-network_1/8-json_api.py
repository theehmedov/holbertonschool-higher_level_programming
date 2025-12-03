#!/usr/bin/python3
"""Searches for a user by letter using POST and displays JSON result"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    # Komanda sətrindən hərf götür, əgər yoxdursa q=""
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    # POST datası
    data = {'q': letter}

    # POST sorğusu
    response = requests.post(url, data=data)

    try:
        result = response.json()
        if not result:
            print("No result")
        else:
            print(f"[{result['id']}] {result['name']}")
    except ValueError:
        print("Not a valid JSON")
