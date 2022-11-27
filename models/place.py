#!/usr/bin/python3
"""Defines the class Place."""

from models.base_model import BaseModel


class Place(BaseModel):
    """Placee class that inherits from BaseModel.

    Attributes:
        city_id (str): empty string: it will be the City.id
        user_id (str): empty string: it will be the User.id
        name (str): empty string
        description (str): empty string
        number_rooms (int): 0
        number_bathrooms (int): 0
        max_guest (int): 0
        price_by_night (int): 0
        latitude (float): 0.0
        longitude (float): 0.0
        amenity_ids (list): empty list of strings: it will
            be the list of Amenity.id later
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        if kwargs and kwargs != {}:
            super().__init__(**kwargs)
        else:
            super().__init__()
