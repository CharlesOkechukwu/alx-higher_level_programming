#!/usr/bin/python3
"""Test the class base which is the base class
Test instantiation and class attributes of the
Base class
"""
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """"Test all attributes and method of the
    Base class using a unittet
    """
    def test_increment(self):
        """Test when no argument is passed to object
        instance and test how id is incremented
        """
        base1 = Base()
        self.assertEqual(base1.id, 1)

        base2 = Base()
        self.assertEqual(base2.id, 2)

        base3 = Base()
        self.assertEqual(base3.id, 3)

        base4 = Base(None)
        self.assertEqual(base4.id, 4)

    def test_positive(self):
        """Test when positive numbers are passed
        to Base object instance
        """
        base1 = Base(20)
        self.assertEqual(base1.id, 20)

        base2 = Base(5)
        self.assertEqual(base2.id, 5)

        base3 = Base(150)
        self.assertEqual(base3.id, 150)

    def test_negative(self):
        """Test when negative numbers are passed
        to Base object instance
        """
        base1 = Base(-3)
        self.assertEqual(base1.id, -3)

        base2 = Base(-10)
        self.assertEqual(base2.id, -10)

    def test_non_int(self):
        """Test when non integer is passed
        to Base object instance
        """
        base1 = Base("Hello")
        self.assertEqual(base1.id, "Hello")

        base2 = Base(0.5)
        self.assertEqual(base2.id, 0.5)
