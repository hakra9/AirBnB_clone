#!/usr/bin/python3
"""

basemodel class that defines all common attributes/methods for other classes



"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """
    BaseModel class is the parent class for AirBnB project
    """

    def __init__(self, *args, **kwargs):
        """intializing the objects variables"""
        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["craeted_at"],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif "__class__":
                    pass
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """saving the objects and updating the saving time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """formating the print statment for basemodel instances"""
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    def to_dict(self):
        """makes a dictionary of an object"""
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return (dic)
