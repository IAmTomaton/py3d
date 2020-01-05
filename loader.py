import struct
from polygon import Polygon
from unit import Unit
import numpy as np


class Loader:

    def load_stl(self, file):
        unit = Unit([])
        with open(file, "rb") as f:
            f.seek(0)
            f.read(84)
            while True:
                byte_polygon = f.read(50)
                if not byte_polygon:
                    break
                unit.add_polygon(self._parse_polygon(byte_polygon))
        return unit

    def _parse_polygon(self, byte_polygon):
        return Polygon([self._parse_vector(byte_polygon[12:24]),
                        self._parse_vector(byte_polygon[24:36]),
                        self._parse_vector(byte_polygon[36:48])],
                       self._parse_vector(byte_polygon[0:12]))

    def _parse_vector(self, byte_vector):
        array = [struct.unpack('<f', byte_vector[i * 4: (i + 1) * 4])[0]
                 for i in range(3)]
        vector = np.array(array)
        return vector
