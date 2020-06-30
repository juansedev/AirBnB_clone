#!/usr/bin/python3
""" This is a test for FileStorage module """


from models.engine.file_storage import FileStorage
from models.engine import file_storage
import pep8
import unittest


class TestFile_Storage(unittest.TestCase):
    """Class for test the FileStorage class"""

    def test_docstring(self):
        """ Method to test doctring module, class and func """
        self.assertTrue(len(file_storage.__doc__) > 0)
        self.assertTrue(len(FileStorage.__doc__) > 0)
        for fn in dir(FileStorage):
            self.assertTrue(len(fn.__doc__) > 0)

    def test_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for func in dir(FileStorage):
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
        file_base = 'models/engine/file_storage.py'
        check = style.check_files([file_base])
        self.assertEqual(check.total_errors, 0, msg)

    def test_is_an_instance(self):
        '''check if my_model is an instance of BaseModel'''
        my_file = FileStorage()
        self.assertIsInstance(my_file, FileStorage)
