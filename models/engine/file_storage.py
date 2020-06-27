#!/usr/bin/python3
""" Module for FileStorage class """


import json
from models.base_model import BaseModel


class FileStorage:
    """ FileStorage class that serializes instances to a
    JSON file and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Creates a new object """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ Serializes a new object to the JSON file"""
        new_file = {}
        for key, value in self.__objects.items():
            new_file[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as jfile:
            json.dump(new_file, jfile)

    def reload(self):
        """ Deserializes all the JSON file to an object """
        try:
            with open(self.__file_path, "r" , encoding="utf-8") as jfile:
                jsonf = json.load(jfile)
            for key, value in jsonf.items():
                value = eval(value["__class__"])(**value)
                self.__objects[key] = value
        except:
            pass
