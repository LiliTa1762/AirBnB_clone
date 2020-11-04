#!/usr/bin/python3
"""
Unittest for BaseModel class
"""


import json
import inspect
from models.base_model import BaseModel
from models import storage
import models
import pep8
import unittest


class Test_BaseModel_Docs(unittest.TestCase):
    """Checking the documentation and style"""
    @classmethod
    def setUpClass(self):
        """Setting for doc tests"""
        self.base_model_funcs = inspect.getmembers(
            BaseModel, inspect.isfunction)

    def test_pep8_conformance_base(self):
        """pep8 tests for BaseModel"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_docstring(self):
        """BaseModel class docstring test"""
        self.assertTrue(len(BaseModel._doc_) >= 1)

    def test_functions_docstrings(self):
        """Presence of docstrings in all functions"""
        for function in self.base_model_funcs:
            self.assertTrue(len(function[1]._doc_) >= 1)


class Test_BaseModel(unittest.TestCase):
    """Checking functionality of BaseModel"""

    def test_a_new_instance_stored(self):
        """New instance stored in objects"""
        self.assertIn(BaseModel(), models.storage.all().values())


if __name__ == '_main_':
    unittest.main()
