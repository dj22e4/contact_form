from utils.commands import add_row, modify_selected_row, delete_selected_row
from utils.constants import BACKGROUND, FOREGROUND, SELECTED
from tkinter import ttk
import tkinter as tk

def create_tree_frame(window):
    tree_frame = tk.Frame(window, background=BACKGROUND)
    tree_frame.pack(padx=10, pady=10, fill='both', expand=True)
    return tree_frame

def create_scrollbars(tree_frame):
    v_scrollbar = ttk.Scrollbar(tree_frame, orient='vertical')
    h_scrollbar = ttk.Scrollbar(tree_frame, orient='horizontal')
    return v_scrollbar, h_scrollbar

def configure_treeview_style():
    style = ttk.Style()
    style.theme_use('default')
    style.configure('Treeview',
                    background=BACKGROUND,
                    foreground=FOREGROUND,
                    fieldbackground=BACKGROUND,
                    rowheight=25,
                    borderwidth=0,
                    relief='flat')
    style.map('Treeview',
               background=[('selected', SELECTED)],
               foreground=[('selected', FOREGROUND)])
    style.configure('Treeview.Heading',
                    background=BACKGROUND,
                    foreground=FOREGROUND,
                    font=('Roboto', 11, 'bold'),
                    borderwidth=0,
                    relief='flat')
    style.map('Treeview.Heading',
              background=[('active', SELECTED)],
              foreground=[('active', FOREGROUND)])
    return style

def create_context_menu(tree):
    context_menu = tk.Menu(tree, tearoff=0, background=BACKGROUND, foreground=FOREGROUND,
                           activebackground=SELECTED, activeforeground=FOREGROUND)
    context_menu.add_command(label='Add Row', command=add_row)
    context_menu.add_command(label='Modify Selected Row', command=modify_selected_row)
    context_menu.add_command(label='Delete Selected Row', command=delete_selected_row)
    def show_context_menu(event):
        item = tree.identify_row(event.y)
        if item:
            tree.selection_set(item)
        context_menu.post(event.x_root, event.y_root)
    tree.bind('<Button-3>', show_context_menu)
    return context_menu

def create_treeview(tree_frame, v_scrollbar, h_scrollbar):
    headers = ('ID', 'Date', 'Last Name', 'First Name', 'Middle Initial',
               'Street Address', 'Apartment #', 'City', 'State', 'Zip Code',
               'Phone #', 'Email', 'Purposes', 'Follow Up Date', 'Comments')
    tree = ttk.Treeview(tree_frame, columns=headers, show='headings', height=8, style='Treeview',
                        yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
    for header in headers:
        tree.heading(header, text=header)
        tree.column(header, width=100, anchor='center')
    tree.grid(row=0, column=0, sticky='nsew')
    v_scrollbar.grid(row=0, column=1, sticky='ns')
    h_scrollbar.grid(row=1, column=0, sticky='ew')
    v_scrollbar.config(command=tree.yview)
    h_scrollbar.config(command=tree.xview)
    tree_frame.grid_rowconfigure(0, weight=1)
    tree_frame.grid_columnconfigure(0, weight=1)
    return tree