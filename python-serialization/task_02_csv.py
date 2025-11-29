#!/usr/bin/python3
"""
json&csv
"""
import csv, json


def convert_csv_to_json(filename):
    try:
        with open(filename) as file:
            reader = csv.DictReader(file)
            data = list(reader)

        json_filename = 'data.json'
        with open(json_filename, 'w') as file:
            json.dump(data, file, indent=4)
            return True

    
    except Exception as e:
        print("file not found: ", e)
        return False
