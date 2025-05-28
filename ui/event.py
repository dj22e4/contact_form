from tkinter import messagebox, filedialog
from db.models import Contact, Purpose
from db.database import Database
from ui.popup import Popup

class EventHandler:
    @staticmethod
    def display_help():
        help_text = (
            'Altar Worker Contact Form\n\n'
            '1. Create a new database via Options > Create Database.\n'
            '2. Open an existing database via Options > Open Database.\n'
            '3. Right-click the table to add, modify, or delete contacts.\n'
            '4. Save changes via Options > Save Database.\n'
            '5. Close the database when done.'
        )
        messagebox.showinfo('Help', help_text)

    @staticmethod
    def display_credits():
        credits_text = (
            'Developed by Duane Ganey Jr.\n'
            'Copyright © 2025'
        )
        messagebox.showinfo('Credits', credits_text)

    @staticmethod
    def add_row(window):
        # TODO: implement
        messagebox.showerror('Error', 'Not implemented yet!')

    @staticmethod
    def modify_selected_row(window):
        # TODO: implement
        messagebox.showerror('Error', 'Not implemented yet!')

    @staticmethod
    def delete_selected_row():
        # TODO: implement
        messagebox.showerror('Error', 'Not implemented yet!')