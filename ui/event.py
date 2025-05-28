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
    def create_database():
        filepath = filedialog.asksaveasfilename(
            defaultextension='.db',
            filetypes=[('SQLite Database', '*.db')]
        )
        try:
            if filepath:
                db = Database(filepath).create()
                messagebox.showinfo('Success', f'Successfully created database at "{filepath}"')
        except Exception as e:
            messagebox.showerror('Error', f'Failed to create database: {e}')

    @staticmethod
    def open_database():
        filepath = filedialog.askopenfilename(
            defaultextension='.db',
            filetypes=[('SQLite Database', '*.db')]
        )
        try:
            if filepath:
                db = Database(filepath).open()
                messagebox.showinfo('Success', f'Successfully opened database at "{filepath}"')
        except Exception as e:
            messagebox.showerror('Error', f'Failed to open database: {e}')

    @staticmethod
    def save_database():
        try:
            db = Database._instance
            db.save()
            messagebox.showinfo('Success', 'Database saved successfully.')
        except Exception as e:
            messagebox.showerror('Error', f'Failed to save database: {e}')

    @staticmethod
    def close_database():
        try:
            db = Database._instance
            db.close()
            messagebox.showinfo('Success', 'Database closed successfully.')
        except Exception as e:
            messagebox.showerror('Error', f'Failed to close database: {e}')

    @staticmethod
    def add_row(window):
        Popup(window, 'Add Row', 300, 300, 'add').render()

    @staticmethod
    def modify_selected_row(window):
        Popup(window, 'Modify Selected Row', 300, 300, 'modify').render()

    @staticmethod
    def delete_selected_row(window):
        # TODO: implement
        messagebox.showerror('Error', 'Not implemented yet!')