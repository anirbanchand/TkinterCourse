from tkinter import *
root=Tk()
root.geometry('500x500')
root.title("Selfie Dance Class")
sname=Label(root,text='Enter Student Name')
age=Label(root,text='Enter Age')
formtype=Label(root,text='Enter type of dance form you want to learn')
sname.grid()
age.grid(row=1)
formtype.grid(row=2)

uservalue=StringVar()
agevalue=StringVar()
formvalue=StringVar()

userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=agevalue)
formentry=Entry(root,textvariable=formvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)
formentry.grid(row=2,column=1)

def getvals():
    with open ('entries.txt','a') as f:
        f.write(f"The student's name is {(uservalue).get()}\n")
        f.write(f"The student's age is {(agevalue).get()}\n")
        f.write(f"The dance form is {(formvalue).get()}\n")

    print('You have registered successfully!')


Button(text='Submit',command=getvals).grid()

root.mainloop()
