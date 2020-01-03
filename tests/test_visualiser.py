import unittest
from visualizer import Visualizer
from polygon import Polygon
import numpy as np


class Test_test_visualiser(unittest.TestCase):

    def test_get_color(self):
        visualizer = Visualizer()
        polygon = Polygon([np.array([0, 0, 0]),
                           np.array([1, 0, 0]),
                           np.array([0, 1, 0])],
                          np.array([0, 0, 1]))

        result = visualizer._get_color(polygon, np.array([1, 0, 0]))

        self.assertEqual(128, result)


if __name__ == '__main__':
    unittest.main()
