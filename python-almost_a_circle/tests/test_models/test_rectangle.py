#!/usr/bin/python3
'''
    test_rectangle.py
    
    Description: Class Rectangle Unittest
'''

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    '''
        Class Rectangle Test Cases
    '''

    def setUp(self):
        '''
            Reset __nb_objects to 0
        '''
        Base._Base__nb_objects = 0

    def test_init_rectangle(self):
        '''
            Test case for Rectangle id
        '''
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.id, 12)

        self.assertRaises(TypeError, Rectangle, 0)
        self.assertRaises(ValueError, Rectangle, 0, 0)
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, -1, 2)

    def test_validator_types(self):
        '''
            Test case for int validator
        '''

        # Getters test
        self.assertRaises(TypeError, Rectangle, "10", 2)
        self.assertRaises(TypeError, Rectangle, 1, [34])
        self.assertRaises(TypeError, Rectangle, 1, 2, "4")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")

        # Setters test
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, 4, 5)
            r1.width = "-2"
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, 4, 5)
            r1.height = "0"
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, 4, 5)
            r1.x = [-1]
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, 4, 5)
            r1.y = (-1, 4)

    def test_validator_values(self):
        '''
            Test for value validator
        '''

        # Setters test
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, -3)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)

        # Setters test
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, 3, 4, 5)
            r1.width = -2
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, 3, 4, 5)
            r1.height = 0
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, 3, 4, 5)
            r1.x = -1
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, 3, 4, 5)
            r1.y = -1

    def test_area(self):
        '''
            Test for ractangle area
        '''
        r10 = Rectangle(3, 2)
        self.assertEqual(r10.area(), 6)
        r11 = Rectangle(2, 10)
        self.assertEqual(r11.area(), 20)
        r12 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r12.area(), 56)

    def test_display_without_x_y(self):
        '''
            Test case for display() without x and y
        '''
        r = Rectangle(2, 3)
        self.assertEqual(r.display(), None)

    def test_display_without_y(self):
        '''
            Test case for display() without y
        '''
        r = Rectangle(2, 3, 1)
        self.assertEqual(r.display(), None)

    def test_display(self):
        '''
            Test case for display()
        '''
        r = Rectangle(2, 3, 1, 2)
        self.assertEqual(r.display(), None)

    def test_str_representation(self):
        '''
            Test for Rectangle string representation
        '''
        r1 = Rectangle(1, 2, 3, 4, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (10) 3/4 - 1/2")

    def test_update(self):
        '''
            Test for update
        '''
        r1 = Rectangle(5, 2, 6, 7)
        r1.update(height=1, id=5)
        self.assertEqual(r1.__str__(), "[Rectangle] (5) 6/7 - 5/1")
        r2 = Rectangle(1, 5, 3, 3, 10)
        r2.update(15, 10, id=5)
        self.assertEqual(r2.__str__(), "[Rectangle] (15) 3/3 - 10/5")
        r3 = Rectangle(1, 3)
        r3.update(id=3, x=4, y=4, width=2, height=3)
        self.assertEqual(r3.__str__(), "[Rectangle] (3) 4/4 - 2/3")

    def test_to_dictionary(self):
        '''
            Test for Rectangle dict representation
        '''
        r1 = Rectangle(10, 9, 1, 2, 5)
        dictionary = {
            'id': 5,
            'width': 10,
            'height': 9,
            'x': 1,
            'y': 2
        }
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, dictionary)

    def test_save_to_file_none(self):
        '''
            Test for Square save_to_file with None
        '''
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file(self):
        '''
            Test for Rectangle save_to_file
        '''
        list_of_dict = [
            {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8},
            {'id': 2, 'width': 2, 'height': 4, 'x': 0, 'y': 0}
        ]
        json_expected = Rectangle.to_json_string(list_of_dict)
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), json_expected)


if __name__ == "__main__":

    unittest.main()
