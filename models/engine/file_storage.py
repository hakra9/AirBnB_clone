#!/user/bin/python3 
"""MOdule"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """serializes ins to a JSON file and deserializes JSON file to ins"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        name = obj.__class__.__name__
        self.__objects["{}.{}".format(name, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file """
        odict = self.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(self.__file_path, "w") as f:
            json.dump(objdict, f)

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
