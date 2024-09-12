from tkinter import *
root = Tk()
root.title("Tell me your honest opinion")
root.geometry("700x500")
def name():
    print("My name is Ani")

def reason():
    print("because the harry bhai's comment setion is most humbel comment section")

def openion():
    print("Harry bhai is one of the best programmer i have ever seen")

def josh():
    print("I am going to complete this course ASAP very positivly")

frame1 = Frame(root, borderwidth=5, background="black", relief=SUNKEN)
frame1.pack(side=LEFT, anchor=N, padx=5)
Button1 = Button(frame1, text="what is your name?", fg="black",font="arial 10 bold", command=name )
Button1.pack(side=LEFT)

frame2 = Frame(root, borderwidth=5, background="black", relief=SUNKEN)
frame2.pack(side=LEFT, anchor=N, padx=5)
Button2 = Button(frame2, text="why are you here?", fg="black",font="arial 10 bold", command=reason )
Button2.pack(side=LEFT)

frame3 = Frame(root, borderwidth=5, background="black", relief=SUNKEN)
frame3.pack(side=LEFT, anchor=N, padx=5)
Button3 = Button(frame3, text="What is your openion about harry bhai", fg="black",font="arial 10 bold", command=openion )
Button3.pack(side=LEFT)

frame4 = Frame(root, borderwidth=5, background="black", relief=SUNKEN)
frame4.pack(side=LEFT, anchor=N, padx=5)
Button4 = Button(frame4, text="How the josh!", fg="black",font="arial 10 bold", command=josh )
Button4.pack(side=LEFT)
root.mainloop()
