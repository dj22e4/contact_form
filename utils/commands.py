from db.models import Base, Contact, Purpose
from tkinter import messagebox, filedialog
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

tree = None
engine = None
Session = None
session = None

def create_database():
    global engine, Session, session
    try:
        filepath = filedialog.asksaveasfilename(
            defaultextension='.db',
            filetypes=[('SQLite Database', '*.db'), ('All Files', '*.*')]
        )
        if not filepath:
            return
        engine = create_engine(f'sqlite:///{filepath}')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        default_purposes = ['Salvation', 'Baptism of the Holy Spirit',
                            'Rededication', 'Healing', 'Other']
        for purpose_name in default_purposes:
            purpose = Purpose(name=purpose_name)
            session.add(purpose)
        session.commit()
        messagebox.showinfo('Success', f'Database created successfully at {filepath}')
    except Exception as e:
        messagebox.showerror('Error', f'Failed to create database: {e}')

def open_database():
    global engine, Session, session
    try:
        filepath = filedialog.askopenfilename(
            filetypes=[('SQLite Database', '*.db'), ('All Files', '*.*')]
        )
        if not filepath:
            return
        if session:
            session.close()
        engine = create_engine(f'sqlite:///{filepath}')
        Session = sessionmaker(bind=engine)
        session = Session()
        messagebox.showinfo('Success', f'Database opened successfully from {filepath}')
    except Exception as e:
        messagebox.showerror('Error', f'Failed to open database: {e}')

def save_database():
    global session
    try:
        if session:
            session.commit()
            messagebox.showinfo('Success', 'Database saved successfully!')
            return
        messagebox.showerror('Error', 'No database is open!')
    except Exception as e:
        messagebox.showerror('Error', f'Failed to save database: {e}')

def close_database(): 
    global engine, Session, session
    try:
        if session:
            session.commit()
            session.close()
            engine = None
            Session = None
            session = None
            messagebox.showinfo('Success', 'Database closed successfully!')
            return
        messagebox.showerror('Error', 'No database is open!')
    except Exception as e:
        messagebox.showerror('Error', f'Failed to close database: {e}')

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

def display_credits():
    credits_text = (
        'Developed by Duane Ganey Jr.\n'
        'Copyright © 2025'
    )
    messagebox.showinfo('Credits', credits_text)

def add_row():
    # TODO: implement
    messagebox.showerror('Error', 'Not implemented yet!')

def modify_selected_row():
    # TODO: implement
    messagebox.showerror('Error', 'Not implemented yet!')

def delete_selected_row():
    global session, tree
    try:
        selected = tree.selection()
        if not selected:
            messagebox.showerror('Error', 'No row selected!')
            return
        item_id = tree.item(selected[0])['values'][0]
        confirm = messagebox.askyesno('Confirm Deletion', 'Are you sure you want to delete this row?')
        if not confirm:
            return
        contact = session.query(Contact).filter(Contact.id == item_id).first()
        if contact:
            session.delete(contact)
            session.commit()
            tree.delete(selected[0])
            messagebox.showinfo('Success', 'Row deleted successfully!')
            return
        messagebox.showerror('Error', 'Row not found in the database!')
    except Exception as e:
        messagebox.showerror('Error', f'Failed to delete row: {e}')