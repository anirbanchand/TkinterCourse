from tkinter import *
from tkinter import messagebox, StringVar, OptionMenu, Checkbutton

root=Tk()
root.geometry("500x500")
root.title("Registration Form")
root.configure(bg="lightblue")

fn=StringVar()
ln=StringVar()
dob=StringVar()
var=StringVar()

var_c1="Java"
var_c2="Python"
var_c3="c++"
radio_var=StringVar()


def printentry():
    first=fn.get()
    last=ln.get()
    date=dob.get()
    var1=var.get()
    var3=var_c1
    var3=var_c2
    var3=var_c3
    var4=radio_var.get()

    print(f"First Name: {first}")
    print(f"Last Name: {last}")
    print(f"Date of Birth: {date}")
    print(f"your country is: {var1}")
    print(f"Programming Language: {var3}")
    print(f"Gender: {var4}")

    messagebox.showinfo("Registration Form", "Registration Successful!")

heading=Label(root, text="Registration Form", font="Arial 15 bold", bg="lightblue",fg="black").grid(row=0,column=4,pady=10)

fname=Label(root, text="First Name", bg="lightblue", fg="black").grid(row=1, column=2)
lname=Label(root, text="Last Name", bg="lightblue", fg="black").grid(row=2, column=2)

efname=Entry(root, textvariable=fn).grid(row=1, column=3)
elname=Entry(root, textvariable=ln).grid(row=2, column=3)

dob=Label(root, text="Date of Birth", bg="lightblue", fg="black").grid(row=3, column=2)
dobentry=Entry(root, textvariable=dob).grid(row=3, column=3)

country=Label(root, text="Country", bg="lightblue", fg="black").grid(row=4, column=2)
list1=['India', 'USA', 'UK', 'France', 'Australia']
droplist=OptionMenu(root, var, *list1)
droplist.config(width=12)
var.set('select country')
droplist.grid(row=4, column=3)


Label(root, text="Programming Language", bg="lightblue", fg="black").grid(row=5, column=2)
c1= Checkbutton(root, bg="lightblue", fg="black",text="Java", variable=var_c1).grid(row=5, column=3)
c2= Checkbutton(root,bg="lightblue", fg="black", text="Python", variable=var_c2).grid(row=6, column=3)
c3= Checkbutton(root, bg="lightblue", fg="black", text="C++", variable=var_c3).grid(row=7, column=3)








root.mainloop()


