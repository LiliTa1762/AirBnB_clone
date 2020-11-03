#!/usr/bin/python3
"""
Class that that defines all common attributes/methods
"""

from datetime import datetime
import models
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Base class from next classes will be based on"""
    def __init__(self, *args, **kwargs):
        """Instantiation instance attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, time)
                if key != '__class__':
                    setattr(self, key, value)

        else:
            now = datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = now
            self.updated_at = now
            models.storage.new(self)

    def __str__(self):
        """To print with a nice format

        Returns:
            [string]: [name, id, and dict]
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """
        Update the public instance attribute
        every time the object is changed
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values"""
        new_dic = self.__dict__.copy()
        new_dic['__class__'] = self.__class__.__name__
        new_dic['created_at'] = self.created_at.isoformat()
        new_dic['updated_at'] = self.updated_at.isoformat()
        return new_dic
