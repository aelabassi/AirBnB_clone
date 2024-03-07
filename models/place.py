#!/usr/bin/python3
from models.base_model import BaseModel

"""
Place class
"""


class Place(BaseModel):
    """ SubClass of BaseModel """
    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
