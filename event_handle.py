from tkinter import *

root=Tk()

def click(event):
    print(f"clicked at, {event.x}, {event.y}")
root.title("Event Handle")
root.geometry("600x400")

widget=Button(root,text="click me please")
widget.pack()

widget.bind('<Button-1>', click)
widget.bind('<Double-1>', quit)

root.mainloop()
