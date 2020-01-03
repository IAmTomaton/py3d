import numpy as np


class Straight:

    def __init__(self, point_a, point_b):
        self._coefficient_y = (point_b[0] - point_a[0]) / (point_b[1] - point_a[1])
        self._bias_y = point_a[0] - point_a[1] * self._coefficient_y

    def get_x(self, y):
        return y * self._coefficient_y + self._bias_y
