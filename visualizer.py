import numpy as np
import math
from plane import Plane
from pixel import Pixel
from straight import Straight


class Visualizer:

    def visualize(self, polygons, light, size):
        matrix = [[Pixel() for i in range(size[1])] for j in range(size[0])]
        for polygon in polygons:
            if polygon is None:
                continue
            color = self._get_color(polygon, light)
            points = polygon.points
            points = sorted(points, key=lambda point: (-point[1], point[0]))
            plane = Plane(points)
            if plane.get_coefficient_z() == 0:
                continue
            if points[0][1] != points[1][1]:
                first_straight = Straight(points[0], points[1])
                second_straight = Straight(points[0], points[2])
                self._set_triangle(points[0][1], points[1][1],
                                   first_straight, second_straight,
                                   plane, matrix, color)
            if points[1][1] != points[2][1]:
                first_straight = Straight(points[1], points[2])
                second_straight = Straight(points[0], points[2])
                self._set_triangle(points[1][1], points[2][1],
                                   first_straight, second_straight,
                                   plane, matrix, color)
        if light[2] < 0:
            width = len(matrix)
            height = len(matrix[0])
            x = int(light[0] + width / 2)
            y = int(height / 2 - light[1])
            self._set_pixel(x, y, 0, matrix, (255, 0, 0))

        return matrix

    def _set_triangle(self, y, max_y,
                      first_straight, second_straight,
                      plane, matrix, color):
        while y >= max_y:
            first_x = first_straight.get_x(y)
            second_x = second_straight.get_x(y)
            x_x = [first_x, second_x]
            x_x.sort()
            self._set_line(y, x_x, plane, matrix, color)
            y -= 1

    def _set_line(self, y, x_x, plane, matrix, color):
        width = len(matrix)
        height = len(matrix[0])
        x_start = int(x_x[0] + width / 2)
        x_end = int(x_x[1] + width / 2)
        y = int(height / 2 - y)
        while x_start <= x_end:
            depth = plane.get_z(x_start, y)
            self._set_pixel(x_start, y, depth, matrix, (color, color, color))
            x_start += 1

    def _set_pixel(self, x, y, depth, matrix, color):
        width = len(matrix)
        height = len(matrix[0])
        if 0 <= x < width and 0 <= y < height:
            pixel = matrix[x][y]
            if depth <= 0 and (pixel.depth == 1 or pixel.depth < depth):
                pixel.depth = depth
                pixel.color = color

    def _get_color(self, polygon, light):
        ray = light - polygon.centre
        cos = np.dot(polygon.normal, ray) /\
            math.sqrt(np.dot(polygon.normal, polygon.normal)) /\
            math.sqrt(np.dot(ray, ray))
        color = 192 - int(128 * (cos + 1) / 2)
        return color
