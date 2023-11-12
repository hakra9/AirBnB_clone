#!/usr/bin/python3
"""
Filestorage class that is responsible for serializing and deserializing 
the jsonfiles 

"""

import json
from models.base_model import BaseModel


class FileStorage():

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the objects dictionary"""
        return (self.__objects)

    def new(self, obj):
        """adds new objects to the objects dictionar"""
        if obj:
            self.__objects["{}.{}".format(
                obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """save the objects to a json file"""
        obj_dict = {}

        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """reads the objects dictionary in json file then turns it to objects"""
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
            for key, value in obj_dict.items():
                obj = BaseModel(**value)
                self.__objects[key] = obj

        except FileNotFoundError:
            pass
