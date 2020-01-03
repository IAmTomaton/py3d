import unittest
from straight import Straight
import numpy as np


class Test_test_straight(unittest.TestCase):

    def test_get_x(self):
        straight = Straight(np.array([1, 1, 0]),
                            np.array([0, 0, 0]))

        result = straight.get_x(2)

        self.assertEqual(2, result)


if __name__ == '__main__':
    unittest.main()
