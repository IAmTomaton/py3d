import unittest
from plane import Plane
import numpy as np


class Test_test_plane(unittest.TestCase):

    def test_contains(self):
        plane = Plane([np.array([1, 0, 0]),
                       np.array([0, 0, 0]),
                       np.array([0, 1, 0])])

        result = plane(np.array([1, 0, 0]))

        self.assertEqual(0, result)

    def test_not_contains(self):
        plane = Plane([np.array([1, 0, 0]),
                       np.array([0, 0, 0]),
                       np.array([0, 1, 0])])

        result = plane(np.array([1, 1, 1]))

        self.assertEqual(-1, result)


if __name__ == '__main__':
    unittest.main()
