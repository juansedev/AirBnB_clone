#!/usr/bin/python3
"""In this module BaseModel class is created"""


from datetime import datetime
import uuid


class BaseModel:
    """This is the BaseModel class from which the other classes will inherit"""

    def __init__(self, *args, **kwargs):
        """Initialization"""
        if kwargs:
            for key, value in kwargs.items():
                if key is not "__class__":
                    if key is "created_at" or key is "updated_at":
                        value = datetime.\
                            strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of an object"""
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the current datetime of 'updated_at' field"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary with all keys/values of
        __dict__ of the instance
        """
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
