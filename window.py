import tkinter as tk
from tkinter import Button, Label, Tk
from PIL.ImageTk import PhotoImage
import numpy as np
from math import sin, cos, pi


class Window:

    def __init__(self, space):
        self._space = space
        self._root = Tk()

        self._init_gui()

        self._root.mainloop()

    def _init_gui(self):
        self._label = Label(self._root)
        self._label.grid(row=0, column=0, rowspan=6)
        self._update_image()

        button_up = Button(self._root, text="up",
                           command=lambda: self.move_camera([0, 1, 0]))
        button_up.grid(row=0, column=2)

        button_down = Button(self._root, text="down",
                             command=lambda: self.move_camera([0, -1, 0]))
        button_down.grid(row=2, column=2)

        button_left = Button(self._root, text="left",
                             command=lambda: self.move_camera([-1, 0, 0]))
        button_left.grid(row=1, column=1)

        button_right = Button(self._root, text="right",
                              command=lambda: self.move_camera([1, 0, 0]))
        button_right.grid(row=1, column=3)

        button_forward = Button(self._root, text="forward",
                                command=lambda: self.move_camera([0, 0, -1]))
        button_forward.grid(row=0, column=4)

        button_back = Button(self._root, text="back",
                             command=lambda: self.move_camera([0, 0, 1]))
        button_back.grid(row=2, column=4)

        button_turn_up = Button(self._root, text="turn_up",
                           command=lambda: self.turn_camera_x(1))
        button_turn_up.grid(row=3, column=2)

        button_turn_down = Button(self._root, text="turn_down",
                             command=lambda: self.turn_camera_x(-1))
        button_turn_down.grid(row=5, column=2)

        button_turn_left = Button(self._root, text="turn_left",
                                  command=lambda: self.turn_camera_y(1))
        button_turn_left.grid(row=4, column=1)

        button_turn_right = Button(self._root, text="turn_right",
                              command=lambda: self.turn_camera_y(-1))
        button_turn_right.grid(row=4, column=3)

        button_show_basis = Button(self._root, text="show_basis",
                                   command=self.show_basis)
        button_show_basis.grid(row=3, column=4)

        button_reset_basis = Button(self._root, text="reset_basis",
                                    command=self.reset_basis)
        button_reset_basis.grid(row=4, column=4)

    def move_camera(self, vector):
        step = 4
        camera = self._space.camera
        camera.move(camera.get_x() * step * vector[0])
        camera.move(np.array([0, 1, 0]) * step * vector[1])
        camera.move(camera.get_z() * step * vector[2])
        self._update_image()

    def turn_camera_y(self, direction):
        angle = pi / 4 * direction
        self._space.camera.turn_y(angle)
        self._update_image()

    def turn_camera_x(self, direction):
        return
        angle = pi / 4 * direction
        self._space.camera.turn_x(angle)
        self._update_image()

    def show_basis(self):
        print(self._space.camera.basis)
        print(self._space.camera.position)

    def reset_basis(self):
        self._space.camera.reset()
        self._update_image()

    def _update_image(self):
        new_image = self._space.get_image()
        self._image = PhotoImage(new_image)
        self._label.configure(image=self._image)
        self._label.configure(width=new_image.width, height=new_image.height)
