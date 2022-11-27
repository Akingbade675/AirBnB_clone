#!/usr/bin/python3
"""Defines the class City."""

from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel.

    Attributes:
        state_id (str): it will be State.id
        name (str): empty string
    """
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        if kwargs and kwargs != {}:
            super().__init__(**kwargs)
        else:
            super().__init__()
