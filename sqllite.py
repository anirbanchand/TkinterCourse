from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.geometry("500x500")
root.title("Registration Form")
root.configure(bg="lightblue")

# Variables
fn = StringVar()
ln = StringVar()
dob_var = StringVar()
var = StringVar()

# Variables for checkboxes
var_c1 = IntVar()
var_c2 = IntVar()
var_c3 = IntVar()

# Variable for radio button
radio_var = StringVar()

# Function to display entered information
def database():
    first = fn.get()
    last = ln.get()
    date = dob_var.get()
    country = var.get()

    # Check for programming languages
    programming_languages = []
    if var_c1.get():
        programming_languages.append("Java")
    if var_c2.get():
        programming_languages.append("Python")
    if var_c3.get():
        programming_languages.append("C++")

    gender = radio_var.get()

    try:
        # Establish connection to the SQLite database
        conn = sqlite3.connect('form.db')

        # Creating a table if it doesn't exist
        with conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS STUDENT(
                    Fname TEXT, 
                    Lname TEXT, 
                    DOB DATE, 
                    Country TEXT, 
                    Programming TEXT, 
                    Gender TEXT
                )
            ''')

            # Inserting the values from the form into the STUDENT table
            cursor.execute('''
                INSERT INTO STUDENT (Fname, Lname, DOB, Country, Programming, Gender) 
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (first, last, date, country, ','.join(programming_languages), gender))

            # Committing the changes
            conn.commit()

        # Display success message
        messagebox.showinfo("Registration Form", "Registration Successful!")

    except sqlite3.Error as error:
        messagebox.showerror("Database Error", f"An error occurred: {error}")

    finally:
        # Ensure the connection is closed
        if conn:
            conn.close()


    # Displaying entered values
    # print(f"First Name: {first}")
    # print(f"Last Name: {last}")
    # print(f"Date of Birth: {date}")
    # print(f"Country: {country}")
    # print(f"Programming Languages: {', '.join(programming_languages)}")
    # print(f"Gender: {gender}")
    #
    # # Message box to confirm registration
    # messagebox.showinfo("Registration Form", "Registration Successful!")

# GUI Layout
heading = Label(root, text="Registration Form", font="Arial 15 bold", bg="lightblue", fg="black").grid(row=0, column=4, pady=10)

fname = Label(root, text="First Name", bg="lightblue", fg="black").grid(row=1, column=2)
lname = Label(root, text="Last Name", bg="lightblue", fg="black").grid(row=2, column=2)

efname = Entry(root, textvariable=fn).grid(row=1, column=3)
elname = Entry(root, textvariable=ln).grid(row=2, column=3)

dob_label = Label(root, text="Date of Birth", bg="lightblue", fg="black").grid(row=3, column=2)
dob_entry = Entry(root, textvariable=dob_var).grid(row=3, column=3)

country = Label(root, text="Country", bg="lightblue", fg="black").grid(row=4, column=2)
list1 = ['India', 'USA', 'UK', 'France', 'Australia']
droplist = OptionMenu(root, var, *list1)
droplist.config(width=12)
var.set('select country')
droplist.grid(row=4, column=3)

# Programming Languages Checkboxes
Label(root, text="Programming Language", bg="lightblue", fg="black").grid(row=5, column=2)
c1 = Checkbutton(root, bg="lightblue", fg="black", text="Java", variable=var_c1).grid(row=5, column=3)
c2 = Checkbutton(root, bg="lightblue", fg="black", text="Python", variable=var_c2).grid(row=6, column=3)
c3 = Checkbutton(root, bg="lightblue", fg="black", text="C++", variable=var_c3).grid(row=7, column=3)

# Gender Radio Buttons
gender = Label(root, text="Gender", bg="lightblue", fg="black").grid(row=8, column=2)
r1 = Radiobutton(root, text="Male", bg="lightblue", fg="black", variable=radio_var, value="Male").grid(row=8, column=3)
r2 = Radiobutton(root, text="Female", bg="lightblue", fg="black", variable=radio_var, value="Female").grid(row=9, column=3)

# Submit and Exit buttons
Button(root, text="Submit", bg="grey", command=database).grid(row=10, column=3)
Button(root, text="Exit", bg="grey", command=root.destroy).grid(row=11, column=3)

# Run the GUI event loop
root.mainloop()
