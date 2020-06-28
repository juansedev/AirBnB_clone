#!/usr/bin/python3
""" This module is for Amenity class """


from models.base_model import BaseModel
from models import storage


class Amenity(BaseModel):
    """ This is Amenity class """

    name = ""
