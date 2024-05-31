""" Unit test calculations.py """

import unittest
from foo_param.calculations import calculate_volume

class TestCalculations(unittest.TestCase):

    """ Test methods in calculations.py """

    def test_calculate_volume(self):

        """ Test the volume returned from calculate_volume() """

        self.assertAlmostEqual(calculate_volume(5), 523.59878)
        self.assertAlmostEqual(calculate_volume(6), 904.77868)

    def test_calculate_volume_invalid_radius(self):

        """ Test the errors returned from calculate_volume() """

        with self.assertRaises(ValueError):
            calculate_volume(-1)
        with self.assertRaises(ValueError):
            calculate_volume(0)
        with self.assertRaises(ValueError):
            calculate_volume("string")

if __name__ == '__main__':
    unittest.main()
