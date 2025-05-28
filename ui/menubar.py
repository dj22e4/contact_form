from config import BACKGROUND, FOREGROUND, SELECTED
from ui.event import EventHandler
import tkinter as tk

class Menubar(tk.Frame):
    def __init__(self, window):
        super(Menubar, self).__init__(window)
        self._window = window
        
    def render(self):
        self.config(background=BACKGROUND)
        self._file_menu()
        self._about_menu()
        self.pack(side='top', fill='x')

    def _file_menu(self):
        self._file_button = tk.Menubutton(self, text='Options', background=BACKGROUND, foreground=FOREGROUND,
                                activebackground=SELECTED, activeforeground=FOREGROUND)
        self._file_button.pack(side='left')
        self._file_menu = tk.Menu(self._file_button, tearoff=0, background=BACKGROUND, foreground=FOREGROUND,
                            activebackground=SELECTED, activeforeground=FOREGROUND)
        self._file_menu.add_command(label='Create Database', command=EventHandler.create_database)
        self._file_menu.add_command(label='Open Database', command=EventHandler.open_database)
        self._file_menu.add_command(label='Save Database', command=EventHandler.save_database)
        self._file_menu.add_command(label='Close Database', command=EventHandler.close_database)
        self._file_menu.add_command(label='Exit', command=self._window.quit)
        self._file_button.config(menu=self._file_menu)

    def _about_menu(self):
        self._about_button = tk.Menubutton(self, text='About', background=BACKGROUND, foreground=FOREGROUND,
                                 activebackground=SELECTED, activeforeground=FOREGROUND)
        self._about_button.pack(side='left')
        self._about_menu = tk.Menu(self._about_button, tearoff=0, background=BACKGROUND, foreground=FOREGROUND,
                            activebackground=SELECTED, activeforeground=FOREGROUND)
        self._about_menu.add_command(label='Help', command=EventHandler.display_help)
        self._about_menu.add_command(label='Credits', command=EventHandler.display_credits)
        self._about_button.config(menu=self._about_menu)