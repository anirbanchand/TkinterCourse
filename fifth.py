from tkinter import *
from PIL import Image,ImageTk
root=Tk()

root.title("My First Tkinter Window")
root.geometry("455x255")
photo=PhotoImage(file="tkinter.jpg")

label=Label(image=photo)
label.pack()
root.mainloop()
