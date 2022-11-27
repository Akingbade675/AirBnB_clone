#!/usr/bin/python3
"""Defines the class User."""

from models.base_model import BaseModel


class User(BaseModel):
    """A class User that inherits from BaseModel.

    Attributes:
        email (str): empty string
        password (str): empty string
        first_name (str): empty string
        last_name (str): empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        if kwargs and kwargs != {}:
            super().__init__(**kwargs)
        else:
            super().__init__()
