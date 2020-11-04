#!/usr/bin/python3
"""
Model for base file storage
"""


import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


classes = {"BaseModel": BaseModel, "User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


class FileStorage:
    """Serialize and deserealize JSON files"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key

        Args:
            <obj class name>.id
        """
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize the JSOn file"""
        objects_json = {}
        for key, value in self.__objects.items():
            objects_json[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(objects_json, f)

    def reload(self):
        """Deserialize the JSON file to a dict"""
        try:
            with open(self.__file_path, "r") as f:
                d_obj = json.load(f)
            for k in d_obj:
                self.__objects[k] = classes[d_obj[k]["__class__"]](**d_obj[k])
        except:
            pass
