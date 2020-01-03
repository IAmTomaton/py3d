import numpy as np
import random


class Polygon:

    def __init__(self, points, normal):
        self._points = points
        self._normal = normal
        self._color = random.randint(0, 255)

    @staticmethod
    def empty():
        return Polygon(np.zeros(3), np.zeros(3), np.zeros(3), np.zeros(3))

    @property
    def centre(self):
        return (self._points[0] + self._points[1] + self._points[2]) / 3

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        self._points = value

    @property
    def normal(self):
        return self._normal

    @normal.setter
    def normal(self, value):
        self._normal = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    def __str__(self):
        return "{} {} {} {}".format(self.normal, *self.points)
