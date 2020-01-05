import numpy as np
import numpy.linalg as la
from polygon import Polygon
import math


class Camera:

    def __init__(self, width=64, height=64):
        self._width = width
        self._height = height
        self.reset()

    def reset(self):
        self._basis = np.eye(3)
        self._position = np.zeros(3)

    def project_polygon(self, polygon):
        points = [self.project_point(polygon.points[0]),
                  self.project_point(polygon.points[1]),
                  self.project_point(polygon.points[2])]
        for point in points:
            if point[2] > 0:
                return None
        normal = polygon.normal.dot(self._basis)
        return Polygon(points, normal)

    def project_point(self, point):
        point = point - self._position
        point = point.dot(self._basis)
        return point

    def move(self, vector):
        self._position += vector

    def turn(self, matrix):
        self._basis = self._basis.dot(matrix)

    def turn_y(self, angle):
        turn = np.eye(3)
        turn[0, 0] = math.cos(angle)
        turn[0, 2] = math.sin(angle)
        turn[2, 0] = -math.sin(angle)
        turn[2, 2] = math.cos(angle)
        self._basis = self._basis.dot(turn)

    def turn_x(self, angle):
        vector = self.get_x()

        turn2 = np.eye(3)
        turn2[0, 0] = -vector[0]
        turn2[0, 2] = vector[2]
        turn2[2, 0] = vector[2]
        turn2[2, 2] = vector[0]

        print(turn2)

        turn3 = np.eye(3)
        turn3[1, 1] = math.cos(angle)
        turn3[1, 2] = math.sin(angle)
        turn3[2, 1] = -math.sin(angle)
        turn3[2, 2] = math.cos(angle)

        self._basis = self._basis.dot(la.inv(turn2)).dot(turn3).dot(turn2)

    @property
    def position(self):
        return self._position

    @property
    def basis(self):
        return self._basis

    @property
    def size(self):
        return self._width, self._height

    def get_x(self):
        return np.array([self._basis[0][0],
                         0,
                         self._basis[2][0]])

    def get_z(self):
        return np.array([self._basis[0][2],
                         0,
                         self._basis[2][2]])
