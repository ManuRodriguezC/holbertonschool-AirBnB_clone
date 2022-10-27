#!/usr/bin/python3
from models.amenity import Amenity
import unittest

class TestAmenetyClass(unittest.TestCase):

    def test_user_name(self):
        """test to check user name"""
        User_1 = Amenity()
        self.assertEqual(type(User_1.id), str)
        self.assertTrue(hasattr(User_1, "name"))

if __name__ == "__main__":
    unittest.main()
