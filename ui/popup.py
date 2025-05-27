from tkinter import messagebox, filedialog
import tkinter as tk

class Popup(tk.Toplevel):
    def __init__(self, window, title, width, height):
        super(Popup, self).__init__(window)
        self._window = window
        self._title = title
        self._width = width
        self._height = height

    def _setup(self):
        self.title(self._title)
        self.geometry(f'{self._width}x{self._height}')
        self.transient(self._window)
        self.grab_set()