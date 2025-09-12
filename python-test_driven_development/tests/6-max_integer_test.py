#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_integers_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1, -2, -3, 4]), 4)
        self.assertEqual(max_integer([-5]), -5)

    def test_floats(self):
        self.assertEqual(max_integer([1.2, 2.5, 3.1, 4.7]), 4.7)
        self.assertEqual(max_integer([-1.2, -2.5, -3.1]), -1.2)
        self.assertEqual(max_integer([0.0, -0.1, -0.2]), 0.0)

    def test_mixed_int_float(self):
        self.assertEqual(max_integer([1, 2.5, 3, 4.1]), 4.1)
        self.assertEqual(max_integer([-1, -2.5, -3]), -1)

    def test_large_numbers(self):
        self.assertEqual(max_integer([10e100, 10e200, 10e300]), 10e300)
        self.assertEqual(max_integer([float('-inf'), 0, float('inf')]), float('inf'))
        self.assertEqual(max_integer([float('-inf')]), float('-inf'))

    def test_strings(self):
        self.assertEqual(max_integer("John"), 'o')
        self.assertEqual(max_integer(["John", "Toto", "Alice"]), "Toto")
        self.assertEqual(max_integer(["a", "z", "m"]), "z")

    def test_sequences(self):
        self.assertEqual(max_integer([[1, 2], [3, 4], [2, 3]]), [3, 4])
        self.assertEqual(max_integer([(1, 2), (3, 4), (2, 3)]), (3, 4))

    def test_booleans(self):
        self.assertEqual(max_integer([True, False, True]), True)
        self.assertEqual(max_integer([False, False]), False)

    def test_empty(self):
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer(()))
        self.assertIsNone(max_integer())

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            max_integer(123)
        with self.assertRaises(TypeError):
            max_integer(1, 2)
        with self.assertRaises(TypeError):
            max_integer([1, "a", 3])


if __name__ == '__main__':
    unittest.main()
