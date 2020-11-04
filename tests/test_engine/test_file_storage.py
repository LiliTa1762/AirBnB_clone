#!/usr/bin/python3
"""
Unittest for FileStorage class
"""


from models.file_storage import FileStorage
import json
import inspect
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
        self.assertTrue(len(FileStorage._doc_) >= 1)

    def test_functions_docstrings(self):
        """Presence of docstrings in all functions"""
        for function in self.file_storage_funcs:
            self.assertTrue(len(function[1]._doc_) >= 1)


class Test_FileStorage(unittest.TestCase):
    """Checking functionality of FileStorage"""

    def test_a_from_json_None(self):
        """JSON with a None String"""
        self.assertEqual([], FileStorage.test_b_from_json_None)


if _name_ == '_main_':
    unittest.main()
