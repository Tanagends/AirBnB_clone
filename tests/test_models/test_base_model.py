#!/usr/bin/python3
"""
This is the module for BaseModel unittest.
"""
import os
import unittest
from models.base_model import BaseModel



class TestBasemodel(unittest.TestCase):
    """
    Unittest for the BaseModel.
    """

    def setUp(self):
        """
        Setup for temporary file path.
        """
        try:
            os.rename("file.json", "temp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """
        Tear down for temporary file path.
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("temp.json", "file.json")
        except FileNotFoundError:
            pass
    def test_init(self):
        """
        The test for the init.
        """
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        """
        The test for the save method.
        """
        my_model = BaseModel()

        initial_updated_at = my_model.updated_at

        current_updated_at = my_model.save()

        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dict(self):
        """
        The test for the to_dict method.
        """
        my_model = BaseModel()

        my_model_dict = my_model.to_dict()

        self.assertIsInstance(my_model_dict, dict)

        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict["updated_at"], my_model.created_at.isoformat())


    def test_str(self):
        """
        The test for the string representation.
        """
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith('[BaseModel]'))

        self.assertIn(my_model.id, str(my_model))

        self.assertIn(str(my_model.__dict__), str(my_model))


if __name__ == "__main__":
    unittest.main()
