from tkinter import *

root = Tk()
root.geometry("300x600")

# Title
root.title("Dance Form")

# Function for logging user data in file
def log():
    with open("Userdetail.txt", "a") as f:
        f.write(f"\nName: {namevar.get()}")
        f.write(f"\nGender: {gendervar.get()}")
        f.write(f"\nFather Name: {fnamevar.get()}")
        f.write(f"\nMother Name: {mnamevar.get()}")
        f.write(f"\nAge: {agevar.get()}")
        f.write(f"\nAddress: {addressvar.get()}\n")

# Variables
namevar = StringVar()
fnamevar = StringVar()
mnamevar = StringVar()
agevar = StringVar()
addressvar = StringVar()
gendervar = StringVar()

# Labels and Entries
gender = Label(root, text="Gender").grid(row=0, column=0, padx=30)
nameentry = Entry(root, textvariable=gendervar).grid(row=0, column=1)
name = Label(root, text="Name").grid(row=1, column=0, padx=30, pady=20)
nameentry = Entry(root, textvariable=namevar).grid(row=1, column=1)
fname = Label(root, text="Father Name").grid(row=2, column=0, padx=30, pady=20)
fnameentry = Entry(root, textvariable=fnamevar).grid(row=2, column=1)
mname = Label(root, text="Mother Name").grid(row=3, column=0, padx=30, pady=20)
mnameentry = Entry(root, textvariable=mnamevar).grid(row=3, column=1)
age = Label(root, text="Age").grid(row=4, column=0, padx=30, pady=20)
ageentry = Entry(root, textvariable=agevar).grid(row=4, column=1)
address = Label(root, text="Address").grid(row=5, column=0, padx=30, pady=20)
addentry = Entry(root, textvariable=addressvar).grid(row=5, column=1)

# Frame
f1 = Frame(root).grid(pady=20)

# Sumit Button
Button(f1, text="Sumit",padx=50, command=log).grid(column=1)

# Close Button
Button(f1, text="Close", padx=50, command=root.destroy).grid(column=1)

root.mainloop()