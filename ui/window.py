from ui.treeview import create_tree_frame, create_scrollbars, configure_treeview_style, create_treeview, create_context_menu
from ui.menubar import create_menubar_frame, create_file_menu, create_about_menu
from utils.constants import TITLE, WIDTH, HEIGHT, RESIZABLE, BACKGROUND, ICON
from utils import commands
import tkinter as tk

def configure_window():
    window = tk.Tk()
    window.title(TITLE)
    x_offset = (window.winfo_screenwidth() - WIDTH) // 2
    y_offset = (window.winfo_screenheight() - HEIGHT) // 2
    window.geometry(f'{WIDTH}x{HEIGHT}+{x_offset}+{y_offset}')
    window.resizable(RESIZABLE, RESIZABLE)
    window.config(background=BACKGROUND)
    icon = tk.PhotoImage(file=ICON)
    window.iconphoto(True, icon)
    return window

def render_window():
    window = configure_window()
    menubar_frame = create_menubar_frame(window)
    create_file_menu(menubar_frame, window)
    create_about_menu(menubar_frame)
    tree_frame = create_tree_frame(window)
    v_scrollbar, h_scrollbar = create_scrollbars(tree_frame)
    style = configure_treeview_style()
    tree = create_treeview(tree_frame, v_scrollbar, h_scrollbar)
    commands.tree = tree
    create_context_menu(tree)
    window.mainloop()