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
        self._data = {}

    def render(self):
        self._create()
        if self._mode == 'add':
            self._render_add_row()
        elif self._mode == 'modify':
            self._render_modify_row()
        else:
            self._render_filter_row()

    def _create(self):
        self.title(self._title)
        x_offset = (self.winfo_screenwidth() - self._width) // 2
        y_offset = (self.winfo_screenheight() - self._height) // 2
        self.geometry(f'{self._width}x{self._height}+{x_offset}+{y_offset}')
        self.transient(self._window)
        self.grab_set()
        self._frame = tk.Frame(self)
        self._frame.config(background=BACKGROUND)
        self._frame.grid(row=0, column=0, sticky='nsew')

    def _render_add_row(self):
        # TODO: implement
        pass

    def _render_modify_row(self):
        # TODO: implement
        pass

    def _render_filter_row(self):
        # TODO: implement
        pass

    def _submit_add(self):
        # TODO: implement
        pass

    def _submit_modify(self):
        # TODO: implement
        pass

    def _submit_filter(self):
        # TODO: implement
        pass