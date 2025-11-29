#!/usr/bin/python3
"""
pickle
"""
import pickle as pc


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        try:
            with open(filename, "wb") as file:
                pc.dump(self, file)
        except Exception as e:
            print("Err handling: ", e)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as file:
                return pc.load(file)
        except Exception as e:
            print("Err handling: ", e)
            return None
