from config import BACKGROUND, FOREGROUND, SELECTED
from ui.event import EventHandler
from tkinter import ttk
import tkinter as tk

class Treeview(tk.Frame):
    def __init__(self, window):
        super(Treeview, self).__init__(window, background=BACKGROUND)
        self._window = window

    def render(self):
        self._scrollbars()
        self._configure()
        self._tree()
        self._menu()
        self.pack(padx=10, pady=10, fill='both', expand=True)

    def _scrollbars(self):
        self._v_scrollbar = ttk.Scrollbar(self, orient='vertical')
        self._h_scrollbar = ttk.Scrollbar(self, orient='horizontal')

    def _configure(self):
        self._style = ttk.Style()
        self._style.theme_use('default')
        self._style.configure('Treeview',
                        background=BACKGROUND,
                        foreground=FOREGROUND,
                        fieldbackground=BACKGROUND,
                        rowheight=25,
                        borderwidth=0,
                        relief='flat')
        self._style.map('Treeview',
                background=[('selected', SELECTED)],
                foreground=[('selected', FOREGROUND)])
        self._style.configure('Treeview.Heading',
                        background=BACKGROUND,
                        foreground=FOREGROUND,
                        font=('Roboto', 11, 'bold'),
                        borderwidth=0,
                        relief='flat')
        self._style.map('Treeview.Heading',
                background=[('active', SELECTED)],
                foreground=[('active', FOREGROUND)])

    def _tree(self):
        self._headers = ('ID', 'Date', 'Last Name', 'First Name', 'Middle Initial',
                        'Street Address', 'Apartment #', 'City', 'State', 'Zip Code',
                        'Phone #', 'Email', 'Purposes', 'Follow Up Date', 'Comments')
        self._tree = ttk.Treeview(self, columns=self._headers, show='headings', height=8, style='Treeview',
                            yscrollcommand=self._v_scrollbar.set, xscrollcommand=self._h_scrollbar.set)
        for header in self._headers:
            self._tree.heading(header, text=header)
            self._tree.column(header, width=100, anchor='center')
        self._tree.grid(row=0, column=0, sticky='nsew')
        self._v_scrollbar.grid(row=0, column=1, sticky='ns')
        self._h_scrollbar.grid(row=1, column=0, sticky='ew')
        self._v_scrollbar.config(command=self._tree.yview)
        self._h_scrollbar.config(command=self._tree.xview)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def _menu(self):
        self._menu = tk.Menu(self._tree, tearoff=0, background=BACKGROUND, foreground=FOREGROUND,
                            activebackground=SELECTED, activeforeground=FOREGROUND)
        self._menu.add_command(label='Add Row', command=lambda: EventHandler.add_row(self._window))
        self._menu.add_command(label='Modify Selected Row', command=lambda: EventHandler.modify_selected_row(self._window))
        self._menu.add_command(label='Delete Selected Row', command=lambda: EventHandler.delete_selected_row(self._window))
        def helper(event):
            item = self._tree.identify_row(event.y)
            if item:
                self._tree.selection.set(item)
            self._menu.post(event.x_root, event.y_root)
        self._tree.bind('<Button-3>', helper)

    def _refresh_fields(self):
        pass