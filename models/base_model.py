#!/usr/bin/python3
"""Defines a class BaseModel."""

import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """
    Defines all common attributes/methods for other classes

    Attributes:
        id (str): assign with an uuid when an instance is created.
        created_at (datetime):  assign with the current datetime
        when an instance is created.
        updated_at (datetime): assign with the current datetime when
        an instance is created and it will be updated every time you
        change your object.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new object from the class.
        """
        if kwargs and kwargs != {}:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            storage.new(self)

    def __str__(self):
        """Returns the string representation of an object."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of
        __dict__ of the instance.
        """
        dicts = dict(self.__dict__)

        dicts["__class__"] = self.__class__.__name__
        dicts["created_at"] = dicts["created_at"].isoformat()
        dicts["updated_at"] = dicts["updated_at"].isoformat()

        return (dicts)
