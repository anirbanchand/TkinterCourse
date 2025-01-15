import tkinter as tk
from tkinter import ttk

def on_select(value):
    print("Selected:", value)

# Create the main window
root = tk.Tk()
root.title("Dropdown Wrapping Example")
root.geometry("200x200")  # Set the window size

# Create a list of options for the dropdown
options = ["Option 1 new option new option", "Option 2 new option new option", "Option 3 new option new option", "Option 4", "Option 5"]

# Create a Tkinter variable to store the selected value
selected_value = tk.StringVar(value=options[0])  # Default value

# Create the dropdown menu
dropdown = ttk.OptionMenu(root, selected_value, *options, command=on_select)
dropdown.pack(padx=10, pady=10, fill='x')  # Wraps horizontally to fit the window size

# Add a label to display the selected value
label = tk.Label(root, textvariable=selected_value)
label.pack(pady=10)

# Run the application
root.mainloop()
