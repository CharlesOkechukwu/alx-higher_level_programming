#!/usr/bin/python3
"""Rectangle test module for unittest
of the rectangle class
"""
from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestRectangle(unittest.TestCase):
    """Unittest cases of Rectangle class
    test all attributes of rectangle
    """
    def test_integer_input(self):
        """test correct integer inputs"""
        r1 = Rectangle(10, 5, 2, 3)
        r2 = Rectangle(6, 3)
        r3 = Rectangle(8, 4, 0, 0, 5)

        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.id, 8)
        self.assertEqual(r2.width, 6)
        self.assertEqual(r2.height, 3)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 9)
        self.assertEqual(r3.id, 5)

    def test_wrong_input(self):
        """test when input is omitted"""
        with self.assertRaises(TypeError):
            r1 = Rectangle()

        with self.assertRaises(TypeError):
            r2 = Rectangle(1)

    def test_instance(self):
        """test if object is instance of class"""
        r1 = Rectangle(6, 2, 0, 0, 4)
        self.assertIsInstance(r1, Base)

    def test_width(self):
        """Test type of input entered for width"""
        with self.assertRaises(TypeError) as r1:
            Rectangle("Hello", 5)
            self.assertEqual(r1.exception, "width must be an ineteger")

        with self.assertRaises(TypeError) as r2:
            Rectangle({"a": 12}, 2)
            self.assertEqual(r2.exception, "width must be an integer")

        with self.assertRaises(TypeError)as r3:
            Rectangle({2, 5}, 2)
            self.assertEqual(r3.exception, "width must be an integer")

        with self.assertRaises(TypeError) as r4:
            Rectangle(1.5, 2)
            self.assertEqual(r4.exception, "width must be an ineteger")

        with self.assertRaises(TypeError) as r5:
            Rectangle(None, 2)
            self.assertEqual(r5.exception, "width must be an integer")

        with self.assertRaises(ValueError) as r6:
            Rectangle(0, 6)
            self.assertEqual(r6.exception, "width must be > 0")

        with self.assertRaises(ValueError) as r7:
            Rectangle(-1, 6)
            self.assertEqual(r7.exception, "width must be > 0")

    def test_height(self):
        """Test type and value of input entered for height"""
        with self.assertRaises(TypeError) as r1:
            Rectangle(5, "Hello")
            self.assertEqual(r1.exception, "height must be an ineteger")

        with self.assertRaises(TypeError) as r2:
            Rectangle(2, {"a": 5})
            self.assertEqual(r2.exception, "height must be an integer")

        with self.assertRaises(TypeError)as r3:
            Rectangle(2, {2, 5})
            self.assertEqual(r3.exception, "height must be an integer")

        with self.assertRaises(TypeError) as r4:
            Rectangle(1, 2.5)
            self.assertEqual(r4.exception, "height must be an ineteger")

        with self.assertRaises(TypeError) as r5:
            Rectangle(1, None)
            self.assertEqual(r5.exception, "height must be an integer")

        with self.assertRaises(ValueError) as r6:
            Rectangle(6, 0)
            self.assertEqual(r6.exception, "height must be > 0")

        with self.assertRaises(ValueError) as r7:
            Rectangle(1, -6)
            self.assertEqual(r7.exception, "height must be > 0")

    def test_x(self):
        """Test type of input entered for width"""
        with self.assertRaises(TypeError) as r1:
            Rectangle(3, 5, "h")
            self.assertEqual(r1.exception, "x must be an ineteger")

        with self.assertRaises(TypeError) as r2:
            Rectangle(5, 2, {"a": 12})
            self.assertEqual(r2.exception, "x must be an integer")

        with self.assertRaises(TypeError)as r3:
            Rectangle(2, 1, {2, 5})
            self.assertEqual(r3.exception, "x must be an integer")

        with self.assertRaises(TypeError) as r4:
            Rectangle(2, 4, 1.5)
            self.assertEqual(r4.exception, "x must be an ineteger")

        with self.assertRaises(TypeError) as r5:
            Rectangle(2, 4, None)
            self.assertEqual(r5.exception, "x must be an integer")

        with self.assertRaises(ValueError) as r6:
            Rectangle(4, 6, -1)
            self.assertEqual(r6.exception, "x must be >= 0")

        with self.assertRaises(ValueError) as r7:
            Rectangle(1, 3, -15)
            self.assertEqual(r7.exception, "x must be >= 0")

    def test_y(self):
        """Test type of input entered for width"""
        with self.assertRaises(TypeError) as r1:
            Rectangle(2, 5, 0, "Hello")
            self.assertEqual(r1.exception, "y must be an ineteger")

        with self.assertRaises(TypeError) as r2:
            Rectangle(1, 4, 0, {"a": 12})
            self.assertEqual(r2.exception, "y must be an integer")

        with self.assertRaises(TypeError)as r3:
            Rectangle(2, 5, 0, {2, 5})
            self.assertEqual(r3.exception, "y must be an integer")

        with self.assertRaises(TypeError) as r4:
            Rectangle(3, 6, 0, 1.5)
            self.assertEqual(r4.exception, "y must be an ineteger")

        with self.assertRaises(TypeError) as r5:
            Rectangle(4, 8, 0, None)
            self.assertEqual(r5.exception, "y must be an integer")

        with self.assertRaises(ValueError) as r6:
            Rectangle(3, 4, 0, -1)
            self.assertEqual(r6.exception, "y must be >= 0")

        with self.assertRaises(ValueError) as r7:
            Rectangle(5, 10, 0, -15)
            self.assertEqual(r7.exception, "y must be >= 0")

    def test_area(self):
        """test area feature"""
        r1 = Rectangle(2, 4)
        self.assertEqual(r1.area(), 8)

        r2 = Rectangle(2, 5, 1)
        self.assertEqual(r2.area(), 10)

        r3 = Rectangle(10, 25, 0, 0)
        self.assertEqual(r3.area(), 250)

        r4 = Rectangle(9, 8, 0, 1, 15)
        self.assertEqual(r4.area(), 72)
