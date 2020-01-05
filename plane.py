import numpy as np


class Plane:

    def __init__(self, points):
        vector_a = points[1] - points[0]
        vector_b = points[2] - points[0]

        self._normal = np.cross(vector_a, vector_b)

        self._bias = np.dot(self._normal, points[0])

    def __call__(self, point):
        return np.dot(self._normal, point) - self._bias

    def get_z(self, x, y):
        return (self._bias - self._normal[0] * x - self._normal[1] * y) /\
            self._normal[2]

    def get_coefficient_z(self):
        return self._normal[2]
