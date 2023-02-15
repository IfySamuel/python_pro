#!/usr/bin/python3
"""
Unittest FileStorage class
"""
import unittest
import pep8
import os
from models import base_model
from models.base_model import BaseModel
from models.engine import file_storage
from models.engine.file_storage import FileStorage


class TestPep8B(unittest.TestCase):
    """ Test pep8 style validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/engine/file_storage.py'
        file2 = 'tests/test_models/test_engine/test_file_storage.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ check for documentation """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(FileStorage.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(FileStorage.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(FileStorage):
            self.assertTrue(len(func.__doc__) > 0)


class BaseModelclassTests(unittest.TestCase):
    """ Test Case for base_model moudle """

    def setUp(self):
        """ Create instance global  """
        self.ins0 = FileStorage()
        self.ins1 = FileStorage()

    def tearDown(self):
        """ Clean All test case """
        pass

    def test_permissions(self):
        """test read-write-execute permissions"""
        read = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertTrue(exe)

    def test_isinstance(self):
        """ Test if a variable is instance of FileStorage """
        self.assertIsInstance(self.ins0, FileStorage)

    def test_all(self):
        """ The dict return is a dictionary """
        dic = self.ins0.all()
        self.assertEqual(type(dic), dict)
        self.assertIs(dic, self.ins0._FileStorage__objects)


if __name__ == '__main__':
    unittest.main()

# Run Test
# python3 -m unittest discover tests
# python3 -m unittest tests/test_models/test_engine/test_file_storage.py