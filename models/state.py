#!/usr/bin/python3
"""Defines the class State."""

from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel.

    Attributes:
        name (str): empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        if kwargs and kwargs != {}:
            super().__init__(**kwargs)
        else:
            super().__init__()
