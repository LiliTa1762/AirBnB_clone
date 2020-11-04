#!/usr/bin/python3
"""
Unittest for BaseModel class
"""

from base_model import BaseModel
import json
import unittest


class Test_BaseModel(unittest.TestCase):
    """Checking the documentation and style"""
    def test_pep8_conformance_base(self):
        """pep8 tests for base"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_docstring(self):
        """BaseModel class docstring test"""
        self.assertTrue(len(Base.__doc__) >= 1)

if __name__ == '__main__':
    unittest.main()
