import unittest
from camera import Camera
import numpy as np
import math


class Test_test_camera(unittest.TestCase):

    def test_project_point_simple(self):
        camera = Camera()
        point = np.ones(3)

        result = camera.project_point(point)

        self.assertEqual(1, result[0])
        self.assertEqual(1, result[1])
        self.assertEqual(1, result[2])

    def test_project_point_move(self):
        camera = Camera()
        point = np.ones(3)
        camera.move(np.array([1, 2, 3]))

        result = camera.project_point(point)

        self.assertEqual(0, result[0])
        self.assertEqual(-1, result[1])
        self.assertEqual(-2, result[2])

    def test_project_point_turn_y_right(self):
        camera = Camera()
        point = np.array([0, 0, 10])
        angle = math.pi / 2

        camera.turn_y(angle)

        result = camera.project_point(point)

        self.assertAlmostEqual(-10, result[0])
        self.assertAlmostEqual(0, result[1])
        self.assertAlmostEqual(0, result[2])

    def test_project_point_turn_y_left(self):
        camera = Camera()
        point = np.array([0, 0, 10])
        angle = -math.pi / 2

        camera.turn_y(angle)

        result = camera.project_point(point)

        self.assertAlmostEqual(10, result[0])
        self.assertAlmostEqual(0, result[1])
        self.assertAlmostEqual(0, result[2])

    def test_project_point_turn_x(self):
        camera = Camera()
        point = np.array([0, 0, 10])
        angle = math.pi / 2

        camera.turn_x(angle)

        result = camera.project_point(point)

        self.assertAlmostEqual(0, result[0])
        self.assertAlmostEqual(-10, result[1])
        self.assertAlmostEqual(0, result[2])

    def test_project_point_turn_x_and_y(self):
        return
        camera = Camera()
        point = np.array([0, 0, 10])
        angle = math.pi / 2

        camera.turn_y(angle)
        camera.turn_x(angle)

        result = camera.project_point(point)

        print(camera.basis)

        self.assertAlmostEqual(-10, result[0])
        self.assertAlmostEqual(0, result[1])
        self.assertAlmostEqual(0, result[2])

if __name__ == '__main__':
    unittest.main()
