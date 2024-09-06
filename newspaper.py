


from tkinter import *
from PIL import Image, ImageTk

base = Tk()
base.title("Today's Newspaper")
base.geometry("1180x644")
base.minsize(width=300, height=300)

# Header for newspapaer
Header = Frame(base, bg="grey", borderwidth=5, relief=SUNKEN)
Header.pack(side=TOP, fill=X)
t = Label(Header, text="Todays's Newspaper", bg="grey", font="Arial 19 bold italic")
t.pack()

# News 1
f1 = Frame(base, bg="lightblue", borderwidth="3", relief=SUNKEN, highlightbackground="black", highlightthickness=1.5)
f1.pack(fill=X, anchor='nw')

p1 = Image.open("tkinter.jpg")
P1 = ImageTk.PhotoImage(p1)

l1 = Label(f1, image=P1, width=130, height=130)
l1.pack(side=LEFT)
l12 = Label(f1, text='''Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]
Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming.
It is often described as a "batteries included" language due to its comprehensive standard library.''', bg="lightblue",)
l12.pack()

# News 2
f2 = Frame(base, bg="lightblue", borderwidth="3", relief=SUNKEN, highlightbackground="black", highlightthickness=1.5)
f2.pack(fill=X, anchor='nw')

p2 = Image.open("tkinter.jpg")
P2 = ImageTk.PhotoImage(p2)

l2 = Label(f2, image=P2, width=130, height=130)
l2.pack(side=LEFT)
l22 = Label(f2, text='''Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]
Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming.
It is often described as a "batteries included" language due to its comprehensive standard library.''', bg="lightblue",)
l22.pack()

# News 3
f3 = Frame(base, bg="lightblue", borderwidth="3", relief=SUNKEN, highlightbackground="black", highlightthickness=1.5)
f3.pack(fill=X, anchor='nw')

p3 = Image.open("tkinter.jpg")
P3 = ImageTk.PhotoImage(p3)

l3 = Label(f3, image=P3, width=130, height=130)
l3.pack(side=LEFT)
l32 = Label(f3, text='''Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]
Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming.
It is often described as a "batteries included" language due to its comprehensive standard library.''', bg="lightblue",)
l32.pack()

# News 4
f4 = Frame(base, bg="lightblue", borderwidth="3", relief=SUNKEN, highlightbackground="black", highlightthickness=1.5)
f4.pack(fill=X, anchor='nw')

p4 = Image.open("tkinter.jpg")
P4 = ImageTk.PhotoImage(p4)

l4 = Label(f4, image=P4, width=130, height=130)
l4.pack(side=LEFT)
l42 = Label(f4, text='''Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]
Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming.
It is often described as a "batteries included" language due to its comprehensive standard library.''', bg="lightblue",)
l42.pack()

base.mainloop()
