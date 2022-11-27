#!/usr/bin/python3
"""Defines the class Review."""

from models.base_model import BaseModel


class Review(BaseModel):
    """State class that inherits from BaseModel.

    Attributes:
        place_id (str): it will be the Place.id
        user_id (str): it will be the User.id
        text (str): empty string
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        if kwargs and kwargs != {}:
            super().__init__(**kwargs)
        else:
            super().__init__()
