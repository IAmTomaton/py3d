from PIL import Image
from unit import Unit


class Space:

    def __init__(self, camera, light, visualizer, loader):
        self._unit = Unit([])
        self._camera = camera
        self._light = light
        self._visualizer = visualizer
        self._loader = loader

    @property
    def unit(self):
        return self._unit

    @property
    def camera(self):
        return self._camera

    @property
    def light(self):
        return self._light

    @property
    def visualizer(self):
        return self._visualizer

    @unit.setter
    def unit(self, value):
        self._unit = value

    def get_image(self):
        polygons = self.unit.polygons
        camera_polygons = [self.camera.project_polygon(p) for p in polygons]

        light = self._camera.project_point(self._light.position)
        matrix = self.visualizer.visualize(camera_polygons,
                                           light, self.camera.size)
        
        byte = bytearray()
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                color = matrix[j][i].color
                byte.append(color[0])
                byte.append(color[1])
                byte.append(color[2])

        image = Image.frombytes("RGB", (len(matrix), len(matrix[0])),
                                bytes(byte))
        return image

    def load(self, file):
        self._unit = self._loader.load_stl(file)
