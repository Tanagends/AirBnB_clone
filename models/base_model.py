#!/usr/bin/python3
"""The Base Model Module"""
import uuid
from datetime import datetime
import models import storage


class BaseModel:
    """The base model class that defines all the common
       attributes and methods for all the other classes
    """

    def __init__(self, *args, **kwargs):
        """Initializes instance variables"""
        if kwargs is not None and kwargs != {}:
            for name, value in kwargs.items():
                match name:
                    #case "__class__":
                    #    continue
                    case "updated_at" | "created_at":
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                self.__dict__[name] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            #models.storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        #models.storage.save()

    def to_dict(self):
        """Returns a dictionary, __dict__ of the instance"""
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['updated_at'] = str(self.updated_at.isoformat())
        instance_dict['created_at'] = str(self.created_at.isoformat())
        return instance_dict
