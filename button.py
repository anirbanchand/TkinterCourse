from tkinter import *
root = Tk()
root.title("Button")
root.geometry("800x500")

def hello():
    print("Hello tkinter")

def name():
    print("Anirban")

frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame, fg="red", text="Click Me", command=hello)
b1.pack(side=LEFT, padx=23)

b2 = Button(frame, fg="red", text="Tell Me your name", command=name)
b2.pack(side=LEFT, padx=23)

b1 = Button(frame, fg="red", text="Click Me")
b1.pack(side=LEFT, padx=23)

root.mainloop()
