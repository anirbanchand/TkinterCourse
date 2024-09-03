from tkinter import *

root=Tk()
# width x height
root.geometry("422x322")

# width,height
root.minsize(300,100)

# width,height
root.maxsize(1200,1000)

root=Label(text="Anirban is a good boy and this is his first GUI")
root.pack()
root.mainloop()
