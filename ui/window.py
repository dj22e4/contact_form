from config import BACKGROUND, ICON
from ui.treeview import Treeview
from ui.menubar import Menubar
import tkinter as tk

class Window(tk.Tk):
    def __init__(self, title, width, height, resizable):
        super(Window, self).__init__()
        self._title = title
        self._width = width
        self._height = height
        self._resizable = resizable

    def render(self):
        self._setup()
        self._menubar = Menubar(self)
        self._menubar.render()
        self._tree = Treeview(self)
        self._tree.render()
        self.mainloop()

    def _setup(self):
        self.title(self._title)
        x_offset = (self.winfo_screenwidth() - self._width) // 2
        y_offset = (self.winfo_screenheight() - self._height) // 2
        self.geometry(f'{self._width}x{self._height}+{x_offset}+{y_offset}')
        self.resizable(self._resizable, self._resizable)
        self.iconphoto(True, tk.PhotoImage(file=ICON))
        self.config(background=BACKGROUND)