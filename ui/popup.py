from config import BACKGROUND
import tkinter as tk

class Popup(tk.Toplevel):
    def __init__(self, window, title, width, height, mode):
        super(Popup, self).__init__(window)
        if mode not in ('add', 'modify', 'filter'):
            raise ValueError('Invalid popup window mode provided!')
        self._window = window
        self._title = title
        self._width = width
        self._height = height
        self._mode = mode

    def render(self):
        self._create()
        if self._mode == 'add':
            self._render_add_row()
        elif self.mode == 'modify':
            self._render_modify_row()
        else:
            self._render_filter_row()

    def _create(self):
        self.title(self._title)
        self.geometry(f'{self._width}x{self._height}')
        self.transient(self._window)
        self.grab_set()
        self.config(background=BACKGROUND)

    def _render_add_row(self):
        # TODO: implement
        print('Rendering "Add Row" components...')

    def _render_modify_row(self):
        # TODO: implement
        print('Rendering "Modify Row" components...')

    def _render_filter_row(self):
        # TODO: implement
        print('Rendering "Filter Row" components...')