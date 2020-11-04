#!/usr/bin/python3
"""
Unittest for FileStorage class
"""


import json
import inspect
from models.engine.file_storage import FileStorage
import pep8
import unittest


class Test_FileStorage_Docs(unittest.TestCase):
    """Checking the documentation and style"""
    @classmethod
    def setUpClass(self):
        """Setting for doc tests"""
        self.file_storage_funcs = inspect.getmembers(
            FileStorage, inspect.isfunction)

    def test_pep8_conformance_base(self):
        """pep8 tests for FileStorage"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_docstring(self):
        """FileStorage class docstring test"""
        self.assertTrue(len(FileStorage.doc) >= 1)

    def test_functions_docstrings(self):
        """Presence of docstrings in all functions"""
        for function in self.file_storage_funcs:
            self.assertTrue(len(function[1].doc) >= 1)


class Test_FileStorage(unittest.TestCase):
    """Checking functionality of FileStorage"""

    def test_a_storage_type(self):
        """Checks the type of storage"""
        self.assertIsNotNone(self.storage.all())

    def test_check_json_loading(self):
        """Checks if FileStorage works."""
        with open("file.json") as f:
            dic = json.load(f)
            self.assertEqual(isinstance(dic, dict), True)

    def test_b_all(self):
        """Checks the all method is not None"""
        obj = self.storage.all()
        self.assertIsNotNone(obj)

    def test_c_all(self):
        """Checks the type of all method"""
        obj = self.storage.all()
        self.assertEqual(type(obj), dict)


    def test_d_functions(self):
        """Checks if the functions are defined"""
        f = FileStorage()

        self.assertTrue(hasattr(f, 'all'))
        self.assertTrue(hasattr(f, 'new'))
        self.assertTrue(hasattr(f, 'reload'))
        self.assertTrue(hasattr(f, 'save'))

if __name__ == 'main':
    unittest.main()
