#!/usr/bin/python3
"""Module containing save_to_json_file function"""


def class_to_json(obj):
    """Function returning dict of a class"""
    return obj.__dict__
