#!/usr/bin/python3
"""Base model"""

import uuid
from datetime import datetime
from models.engine import file_storage
import models

class BaseModel:
    """
    Base class for all other models.
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.id = kwargs.pop("id", str(uuid.uuid4()))
            self.created_at = datetime.fromisoformat(kwargs.pop("created_at"))
            self.updated_at = datetime.fromisoformat(kwargs.pop("updated_at"))
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dict_repr = self.__dict__.copy()
        dict_repr.update({
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        })
        return dict_repr
