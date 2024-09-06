from tkinter import *
root=Tk()
root.geometry("844x333")
root.title("My GUI")


# ****************important label options**********
# text-adds the text
# bd-background
# fg-foreground
# font-sets the font
# font 2 ways
# 1st way(tuple)- font=("comicsansms", 13, "bold")
# 2nd way(string)- font="comicsansms 13 bold"
# padx-x padding
# pady-y padding
# relief-broder styling-SUNKEN,RAISED,GROOVE,RIDGE

title_label=Label(text='''Tk/Tcl has long been an integral part of Python.\n It provides a robust and platform independent windowing toolkit, that is available to Python programmers using the tkinter package,\n and its extension, the tkinter.tix and the tkinter.ttk modules.\n

The tkinter package is a thin object-oriented layer on top of Tcl/Tk.\n To use tkinter, you don’t need to write Tcl code, but you will need to consult the Tk documentation, and occasionally the Tcl documentation.\n tkinter is a set of wrappers that implement the Tk widgets as Python classes.''', bg="red", fg="white", padx=20, pady=20, font="comicsansms 13 bold", borderwidth=5, relief="solid",highlightthickness=2, highlightbackground="black")


# ************Important Pack options*************

# anchor=nw(north-west),se,sw,ne
# side= top,bottom, left, right(by def: top)
# fill
# padx
# pady


# title_label.pack(anchor="ne")
# title_label.pack(side="bottom", anchor="se",fill=X)
title_label.pack(side="left", anchor="se",fill=Y,padx=20,pady=25)



root.mainloop()
