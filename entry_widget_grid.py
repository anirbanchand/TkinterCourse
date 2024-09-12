from tkinter import *

from tkinter import StringVar

from requests import get

root=Tk()

root.geometry("800x500")
root.title("My GUI")

def getval():
    print(f"The value of username is {uservalue.get()} and the password is {passvalue.get()}")
    # print(get("XXXXXXXXXXXXXXXXXXXXXX").text)

user= Label(root, text="Username")
pwd= Label(root, text="Password")
user.grid()
pwd.grid(row=1)


# variable Classes in Tkinter
# BooleanVar, DoubleVar, FloatVar, IntVar, StringVar

uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root, textvariable=uservalue)
passentry=Entry(root, textvariable=passvalue)
userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)
Button(text="Submit", command=getval).grid()


root.mainloop()
