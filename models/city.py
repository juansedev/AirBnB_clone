#!/usr/bin/python3
""" This module is for City class """


from models.base_model import BaseModel
from models import storage


class City(BaseModel):
    """ This is City class """

    state_id = ""
    name = ""
