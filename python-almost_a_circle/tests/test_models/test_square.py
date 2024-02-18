#!/usr/bin/python3
'''
    test_square.py
    
    Description: Class Square Unittest
'''

import unittest
from models.base import Base
from models.square import Square


class TestRectangle(unittest.TestCase):
    '''
        Class Square Test Cases
    '''

    def setUp(self):
        '''
            Reset __nb_objects to 0
        '''
        Base._Base__nb_objects = 0

    def test_init_rectangle(self):
        '''
            Test case for Square id
        '''
        s1 = Square(1)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

        s2 = Square(1, 2, 3, 4)
        self.assertEqual(s2.size, 1)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertEqual(s2.id, 4)

        self.assertRaises(ValueError, Square, 0)

    def test_validator_types(self):
        '''
            Test case for int validator
        '''

        # Getters test
        self.assertRaises(TypeError, Square, "10", 2)
        self.assertRaises(TypeError, Square, 1, [34])
        self.assertRaises(TypeError, Square, 1, 2, "4")

        # Setters test
        with self.assertRaises(TypeError):
            s1 = Square(1)
            s1.size = "-2"
        with self.assertRaises(TypeError):
            s1 = Square(1)
            s1.x = "-2"
        with self.assertRaises(TypeError):
            s1 = Square(1)
            s1.y = "-2"

    def test_validator_values(self):
        '''
            Test for value validator
        '''

        # Getters test
        self.assertRaises(ValueError, Square, -3, 2)
        self.assertRaises(ValueError, Square, 1, -34)
        self.assertRaises(ValueError, Square, 1, 2, -3)

        # Setters test
        with self.assertRaises(ValueError):
            s1 = Square(1)
            s1.size = -2
        with self.assertRaises(ValueError):
            s1 = Square(1)
            s1.x = -2
        with self.assertRaises(ValueError):
            s1 = Square(1)
            s1.y = -2

    def test_area(self):
        '''
            Test for Square area
        '''
        s1 = Square(3)
        self.assertEqual(s1.area(), 9)
        s2 = Square(4, 10)
        self.assertEqual(s2.area(), 16)
        s3 = Square(2, 7, 6, 10)
        self.assertEqual(s3.area(), 4)

    def test_str_representation(self):
        '''
            Test for square string representation
        '''
        s1 = Square(1, 2, 3, 10)
        self.assertEqual(s1.__str__(), "[Square] (10) 2/3 - 1")

    def test_update(self):
        '''
            Test for update

        '''

        # Test for args
        s1 = Square(1, 2, 3, 4)
        s1.update(10, size=10, x=10, y=10)
        self.assertEqual(s1.__str__(), "[Square] (10) 2/3 - 1")
        s2 = Square(1, 2, 3, 4)
        s2.update(10, 10, x=10, y=10)
        self.assertEqual(s2.__str__(), "[Square] (10) 2/3 - 10")
        s3 = Square(1, 2, 3, 4)
        s3.update(10, 10, 10, y=10)
        self.assertEqual(s3.__str__(), "[Square] (10) 10/3 - 10")
        s4 = Square(1, 2, 3, 4)
        s4.update(10, 10, 10, 10)
        self.assertEqual(s4.__str__(), "[Square] (10) 10/10 - 10")

        # Test for **kwargs
        s1 = Square(1, 2, 3, 4)
        s1.update(id=10)
        self.assertEqual(s1.__str__(), "[Square] (10) 2/3 - 1")
        s2 = Square(1, 2, 3, 4)
        s2.update(id=10, size=10)
        self.assertEqual(s2.__str__(), "[Square] (10) 2/3 - 10")
        s3 = Square(1, 2, 3, 4)
        s3.update(id=10, size=10, x=10)
        self.assertEqual(s3.__str__(), "[Square] (10) 10/3 - 10")
        s4 = Square(1, 2, 3, 4)
        s4.update(id=10, size=10, x=10, y=10)
        self.assertEqual(s4.__str__(), "[Square] (10) 10/10 - 10")

    def test_to_dictionary(self):
        '''
            Test for Square dict representation
        '''
        s1 = Square(10, 2, 1)
        dictionary = {
            'id': 1,
            'size': 10,
            'x': 2,
            'y': 1
        }
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, dictionary)

    def test_save_to_file_none(self):
        '''
            Test for Square save_to_file with None
        '''
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file(self):
        '''
            Test for Square save_to_file
        '''
        list_of_dict = [
            {'id': 1, 'size': 10, 'x': 7, 'y': 2},
            {'id': 2, 'size': 2, 'x': 0, 'y': 0}
        ]

        json_expected = Square.to_json_string(list_of_dict)
        s1 = Square(10, 7, 2)
        s2 = Square(2)
        Square.save_to_file([s1, s2])

        with open("Square.json") as file:
            self.assertEqual(file.read(), json_expected)

    def test_load_from_file(self):
        '''
            Test for load_from_file
        '''
        result = Square.load_from_file()
        self.assertEqual(result, [])

        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4)
        list_rectangles = [s1, s2]

        Square.save_to_file(list_rectangles)

        result = Square.load_from_file()
        self.assertEqual(len(result), 2)


if __name__ == "__main__":

    unittest.main()
