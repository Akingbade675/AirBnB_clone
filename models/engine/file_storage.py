#!/usr/bin/python3
"""Defines the class FileStorage"""

import json


class FileStorage():
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances.

    Attributes:
        file_path (string): path to the JSON file
        objects (dict): empty but will store all objects by <class name>.id
    """

    __file_path = "file.json"
    __objects = {}

    def classes(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'Place': Place,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Review': Review
        }
        return classes

    def all(self):
        """returns the dictionary ```__objects```"""
        return (FileStorage.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w") as json_file:
            if FileStorage.__objects is None:
                json_file.write("{}")
            else:
                list_dict = {}
                for key, value in FileStorage.__objects.items():
                    list_dict[key] = value.to_dict()
                json_file.write(json.dumps(list_dict))

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as json_file:
                list_dict = json.loads(json_file.read())
                for key, value in list_dict.items():
                    class_name, uid = key.split(".")
                    obj = self.classes()[class_name](**value)
                    FileStorage.__objects[key] = obj
        except IOError:
            pass
