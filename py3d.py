from loader import Loader
from space import Space
from camera import Camera
from visualizer import Visualizer
from window import Window
import numpy as np


def main():
    loader = Loader()
    camera = Camera(width=256, height=256)
    light = Camera()
    light.move(np.array([0, 0, -100]))
    visualizer = Visualizer()
    space = Space(camera, light, visualizer, loader)
    space.load("test3.stl")
    window = Window(space)


if __name__ == "__main__":
    main()
