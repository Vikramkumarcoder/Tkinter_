from tkinter import *

root = Tk()
root.geometry("655x333")
root.title("Entry")

def output():
    print(f"Username: {uservalue.get()}")
    print(f"Password: {passvalue.get()}")

user = Label(text="Username").grid()
password = Label(text="Password").grid(row=1)


#Variable class in tkinter
#Booleanvar, stringvar, doublevar, intvar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue).grid(row=0, column=1)
passentry = Entry(root, textvariable=passvalue).grid(row=1, column=1)

# Sumit Button
Button(root, text="sumit", command=output).grid(column=1, pady=22)

# Exit Button
Button(root, text="Exit", command=root.destroy).grid(row=2)
root.mainloop()