from config import BACKGROUND, FOREGROUND, SELECTED
from tkinter import ttk
import tkinter as tk

class Treeview(tk.Frame):
    def __init__(self, window):
        super(Treeview, self).__init__(window, background=BACKGROUND)
        self.window = window

    def render(self):
        self._scrollbars()
        self._configure()
        self._tree()
        self._menu()
        self.pack(padx=10, pady=10, fill='both', expand=True)

    def _scrollbars(self):
        self.v_scrollbar = ttk.Scrollbar(self, orient='vertical')
        self.h_scrollbar = ttk.Scrollbar(self, orient='horizontal')

    def _configure(self):
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure('Treeview',
                        background=BACKGROUND,
                        foreground=FOREGROUND,
                        fieldbackground=BACKGROUND,
                        rowheight=25,
                        borderwidth=0,
                        relief='flat')
        self.style.map('Treeview',
                background=[('selected', SELECTED)],
                foreground=[('selected', FOREGROUND)])
        self.style.configure('Treeview.Heading',
                        background=BACKGROUND,
                        foreground=FOREGROUND,
                        font=('Roboto', 11, 'bold'),
                        borderwidth=0,
                        relief='flat')
        self.style.map('Treeview.Heading',
                background=[('active', SELECTED)],
                foreground=[('active', FOREGROUND)])

    def _tree(self):
        self.headers = ('ID', 'Date', 'Last Name', 'First Name', 'Middle Initial',
                        'Street Address', 'Apartment #', 'City', 'State', 'Zip Code',
                        'Phone #', 'Email', 'Purposes', 'Follow Up Date', 'Comments')
        self.tree = ttk.Treeview(self, columns=self.headers, show='headings', height=8, style='Treeview',
                            yscrollcommand=self.v_scrollbar.set, xscrollcommand=self.h_scrollbar.set)
        for header in self.headers:
            self.tree.heading(header, text=header)
            self.tree.column(header, width=100, anchor='center')
        self.tree.grid(row=0, column=0, sticky='nsew')
        self.v_scrollbar.grid(row=0, column=1, sticky='ns')
        self.h_scrollbar.grid(row=1, column=0, sticky='ew')
        self.v_scrollbar.config(command=self.tree.yview)
        self.h_scrollbar.config(command=self.tree.xview)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def _menu(self):
        self.menu = tk.Menu(self.tree, tearoff=0, background=BACKGROUND, foreground=FOREGROUND,
                            activebackground=SELECTED, activeforeground=FOREGROUND)
        self.menu.add_command(label='Add Row', command=None) # TODO
        self.menu.add_command(label='Modify Selected Row', command=None) # TODO
        self.menu.add_command(label='Delete Selected Row', command=None) # TODO
        def helper(event):
            item = self.tree.identify_row(event.y)
            if item:
                self.tree.selection.set(item)
            self.menu.post(event.x_root, event.y_root)
        self.tree.bind('<Button-3>', helper)