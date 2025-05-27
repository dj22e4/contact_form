from config import BACKGROUND, FOREGROUND, SELECTED
import tkinter as tk

class Menubar(tk.Frame):
    def __init__(self, window):
        super(Menubar, self).__init__(window)
        self.window = window
        
    def render(self):
        self._file_menu()
        self._about_menu()
        self.pack(side='top', fill='x')
        self.config(background=BACKGROUND)

    def _file_menu(self):
        self.file_button = tk.Menubutton(self, text='Options', background=BACKGROUND, foreground=FOREGROUND,
                                activebackground=SELECTED, activeforeground=FOREGROUND)
        self.file_button.pack(side='left')
        self.file_menu = tk.Menu(self.file_button, tearoff=0, background=BACKGROUND, foreground=FOREGROUND,
                            activebackground=SELECTED, activeforeground=FOREGROUND)
        self.file_menu.add_command(label='Create Database', command=None) # TODO
        self.file_menu.add_command(label='Open Database', command=None) # TODO
        self.file_menu.add_command(label='Save Database', command=None) # TODO
        self.file_menu.add_command(label='Close Database', command=None) # TODO
        self.file_menu.add_command(label='Exit', command=self.window.quit)
        self.file_button.config(menu=self.file_menu)

    def _about_menu(self):
        self.about_button = tk.Menubutton(self, text='About', background=BACKGROUND, foreground=FOREGROUND,
                                 activebackground=SELECTED, activeforeground=FOREGROUND)
        self.about_button.pack(side='left')
        self.about_menu = tk.Menu(self.about_button, tearoff=0, background=BACKGROUND, foreground=FOREGROUND,
                            activebackground=SELECTED, activeforeground=FOREGROUND)
        self.about_menu.add_command(label='Help', command=None) # TODO
        self.about_menu.add_command(label='Credits', command=None) # TODO
        self.about_button.config(menu=self.about_menu)