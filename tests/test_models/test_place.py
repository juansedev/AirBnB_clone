#!/usr/bin/python3
""" This is a test module for Place Class"""


from models.place import Place
from models import place
import pep8
import unittest
import os


class TestPlace(unittest.TestCase):
    """Class for test the Place class"""

    def test_docstring(self):
        """ Method to test doctring module, class and func """
        self.assertTrue(len(place.__doc__) > 0)
        self.assertTrue(len(Place.__doc__) > 0)
        for fn in dir(Place):
            self.assertTrue(len(fn.__doc__) > 0)

    def test_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for func in dir(Place):
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0])
                )

    def test_pep8(self):
        """ Test for pep8 stylecode """
        msg = "Found code style errors (and warning)."
        style = pep8.StyleGuide(quiet=True)
        file_base = 'models/place.py'
        check = style.check_files([file_base])
        self.assertEqual(check.total_errors, 0, msg)

    def test_is_an_instance(self):
        '''check if my_place is an instance of BaseModel'''
        my_place = Place()
        self.assertIsInstance(my_place, Place)

    def test_permissions(self):
        """ Test for check the permissions """
        read = os.access('models/place.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/place.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/place.py', os.X_OK)
        self.assertTrue(exe)
