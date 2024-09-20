import sqlite3
from tkinter import *
from tkinter import messagebox

# Create a window
root = Tk()
root.title("Tkinter Database Connection Example")
root.geometry("400x400")

# Connect to SQLite Database (or create it)
def connect_db():
    conn = sqlite3.connect("users.db")  # Database file
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        )
    """)
    conn.commit()
    conn.close()
    messagebox.showinfo("Connection", "Database connected successfully")

# Function to insert user into the database
def insert_user():
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()

    name = entry_name.get()
    age = entry_age.get()

    if name == "" or age == "":
        messagebox.showwarning("Input error", "Please fill all fields")
    else:
        cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        conn.commit()
        conn.close()
        entry_name.delete(0, END)
        entry_age.delete(0, END)
        messagebox.showinfo("Success", "User added successfully")

# Function to display users from the database
def display_users():
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    records = cur.fetchall()
    conn.close()

    display_text = ""
    for record in records:
        display_text += f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}\n"

    result_label.config(text=display_text)

# GUI Widgets
Label(root, text="Name:").pack(pady=5)
entry_name = Entry(root, width=30)
entry_name.pack(pady=5)

Label(root, text="Age:").pack(pady=5)
entry_age = Entry(root, width=30)
entry_age.pack(pady=5)

# Buttons
Button(root, text="Connect to Database", command=connect_db).pack(pady=10)
Button(root, text="Insert User", command=insert_user).pack(pady=10)
Button(root, text="Display Users", command=display_users).pack(pady=10)

# Label to display fetched records
result_label = Label(root, text="")
result_label.pack(pady=10)

# Run the GUI event loop
root.mainloop()
