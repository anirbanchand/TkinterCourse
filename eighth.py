from tkinter import *

root=Tk()

root.geometry=("1999x555")
root.title("Pycharm")
f1=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

f2=Frame(root, bg="grey", borderwidth=8, relief=SUNKEN)
f2.pack(side=TOP, fill="x")

l=Label(f1, text="Project Tkinter - Pycharm")
l.pack(pady=142)

l=Label(f2,text="Welcome to Pycharm", font="Helvetica 16 bold", fg="red")
l.pack()

root.mainloop()
