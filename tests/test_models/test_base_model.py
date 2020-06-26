#!/usr/bin/python3
""" This is a test module for BaseModel Class"""


from models.base_model import BaseModel
import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    """Class for test the BaseModel class"""

    def setUp(self):
        """setUp Method"""
        self.base1 = BaseModel()
        self.base2 = BaseModel()

    def tearDown(self):
        """tearDown Method"""
        pass

    def test_init(self):
        """ Method to test the initialization of instances"""
        self.assertIs(type(self.base1.id), str)
        self.assertIs(type(self.base1.created_at), datetime.datetime)
        self.assertNotEqual(self.base1.id, self.base2.id)
        self.assertEqual(self.base1.created_at, self.base1.updated_at)
        self.assertEqual(self.base2.created_at, self.base2.updated_at)
        self.assertNotEqual(self.base1.created_at, self.base2.created_at)

    def test_str(self):
        """ Method to test __str__ method """
        output = "[BaseModel] ({}) {}".\
            format(self.base1.id, self.base1.__dict__)
        self.assertEqual(str(self.base1), output)
        self.base1.name = "Holberton"
        self.base1.my_number = 89
        output = "[BaseModel] ({}) {}".\
            format(self.base1.id, self.base1.__dict__)
        self.assertEqual(str(self.base1), output)

    def test_to_dict(self):
        """ Method to test to_dict method """
        keys = ['id', 'created_at', 'updated_at', '__class__']
        dict_b1 = self.base1.to_dict()
        self.assertCountEqual(keys, dict_b1)
        self.base1.name = "Holberton"
        self.base1.my_number = 89
        keys = ['id',
                'created_at',
                'updated_at',
                '__class__',
                'name',
                'my_number']
        dict_b1 = self.base1.to_dict()
        self.assertCountEqual(keys, dict_b1)
