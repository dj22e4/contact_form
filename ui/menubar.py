from utils.commands import create_database, open_database, save_database, close_database, display_help, display_credits
from utils.constants import BACKGROUND, FOREGROUND, SELECTED
import tkinter as tk

def create_menubar_frame(window):
    menubar_frame = tk.Frame(window, background=BACKGROUND, height=30)
    menubar_frame.pack(side='top', fill='x')
    return menubar_frame

def create_file_menu(menubar_frame, window):
    file_button = tk.Menubutton(menubar_frame, text='Options', background=BACKGROUND, foreground=FOREGROUND,
                                activebackground=SELECTED, activeforeground=FOREGROUND)
    file_button.pack(side='left')
    file_menu = tk.Menu(file_button, tearoff=0, background=BACKGROUND, foreground=FOREGROUND,
                        activebackground=SELECTED, activeforeground=FOREGROUND)
    file_menu.add_command(label='Create Database', command=create_database)
    file_menu.add_command(label='Open Database', command=open_database)
    file_menu.add_command(label='Save Database', command=save_database)
    file_menu.add_command(label='Close Database', command=close_database)
    file_menu.add_command(label='Exit', command=window.quit)
    file_button.config(menu=file_menu)

def create_about_menu(menubar_frame):
    about_button = tk.Menubutton(menubar_frame, text='About', background=BACKGROUND, foreground=FOREGROUND,
                                 activebackground=SELECTED, activeforeground=FOREGROUND)
    about_button.pack(side='left')
    about_menu = tk.Menu(about_button, tearoff=0, background=BACKGROUND, foreground=FOREGROUND,
                         activebackground=SELECTED, activeforeground=FOREGROUND)
    about_menu.add_command(label='Help', command=display_help)
    about_menu.add_command(label='Credits', command=display_credits)
    about_button.config(menu=about_menu)