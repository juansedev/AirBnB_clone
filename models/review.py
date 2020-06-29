#!/usr/bin/python3
""" This module is for Review class """


from models.base_model import BaseModel
from models import storage


class Review(BaseModel):
    """ This is Review class """

    place_id = ""
    user_id = ""
    text = ""
