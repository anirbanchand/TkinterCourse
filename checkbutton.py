from tkinter import *

from tkinter import Checkbutton

root=Tk()

root.geometry("644x344")

def getval():
    print("it works")

#heading
Label(root, text="Welcome to Anirban Travels",font="comicsansms 19 bold",pady=10).grid(row=0,column=3)

# Text for our form
name=Label(root, text="Name")
phone=Label(root, text="Phone")
gender=Label(root, text="Gender")
emergency=Label(root, text="Emergency Contact")
paymentmode=Label(root, text="Payment Mode")


#pack text for our form
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

# Tkinter variable for storing entries
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()

# Entry for our form
nameentry= Entry(root, textvariable=namevalue)
phoneentry= Entry(root, textvariable=phonevalue)
genderentry= Entry(root, textvariable=gendervalue)
emergencyentry= Entry(root, textvariable=emergencyvalue)
paymentmodeentry= Entry(root, textvariable=paymentmodevalue)

#check box using
food_checkbutton=Checkbutton(text="Want to prebook your meals?", variable=foodservicevalue)

# entry= Entry(root, textvariable=)

# packing the Entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)
food_checkbutton.grid(row=6, column=3)

Button(text="Submit",bg="grey", command=getval).grid(row=7,column=3)



root.mainloop()
