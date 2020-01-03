class Unit:

    def __init__(self, polygons):
        self._polygons = polygons

    @property
    def polygons(self):
        return self._polygons

    @polygons.setter
    def polygons(self, value):
        self._polygons = value

    def add_polygon(self, polygon):
        self._polygons.append(polygon)
