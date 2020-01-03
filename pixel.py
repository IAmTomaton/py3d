class Pixel:

    def __init__(self):
        self._depth = 1
        self._color = (0, 0, 0)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, value):
        self._depth = value
