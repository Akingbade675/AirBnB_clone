#!/usr/bin/python3
"""Defines the class Amenity."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel.

    Attributes:
        name (str): empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        if kwargs and kwargs != {}:
            super().__init__(**kwargs)
        else:
            super().__init__()
