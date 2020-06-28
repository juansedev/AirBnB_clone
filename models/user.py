#!/usr/bin/python3
""" This module is for User class """


from models.base_model import BaseModel
from models import storage


class User(BaseModel):
    """ This is User class """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
