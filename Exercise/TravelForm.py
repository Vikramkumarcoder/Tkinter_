from tkinter import *

root = Tk()
root.geometry("655x333")
root.title("Travel Form")

def store():
    with open("Travel_data.txt", "a") as f:
        f.write(f"\n\nName: {namevar.get()}")
        f.write(f"\nPhone: {phonevar.get()}")
        f.write(f"\nGender: {gendervar.get()}")
        f.write(f"\nEmergency Phone: {emergencyvar.get()}")
        f.write(f"\nPayment Mode: {paymentmodevar.get()}")
        if checkboxvar.get() == 1:
            f.write(f"\nDo he/she want food: YES")
        elif checkboxvar.get()==0:
            f.write(f"\nDo he/she want food: NO\n")


# Label welcome banner
Label(root, text="Welcome to Vikram Airline", font="comicsansms 25 bold").grid(row=0, column=1)

# Text LABELING AND GRIDING
name = Label(root, text="Name", font="comicsansms 15 bold").grid(row=1, column=0)
phone = Label(root, text="Phone", font="comicsansms 15 bold").grid(row=2, column=0)
gender = Label(root, text="Gender", font="comicsansms 15 bold").grid(row=3, column=0)
emergency = Label(root, text="Emergency contacts", font="comicsansms 15 bold").grid(row=4, column=0)
paymentmode = Label(root, text="Payment Mode", font="comicsansms 15 bold").grid(row=5, column=0)

# Entry variables of respective texts
namevar = StringVar()
phonevar = StringVar()
gendervar = StringVar()
emergencyvar = StringVar()
paymentmodevar = StringVar()
checkboxvar = IntVar()

# Entries and pack with grid
nameentry = Entry(root, textvariable=namevar).grid(row=1, column=1)
pnoneentry = Entry(root, textvariable=phonevar).grid(row=2, column=1)
genderentry = Entry(root,textvariable=gendervar).grid(row=3, column=1)
emergencyentry = Entry(root, textvariable=emergencyvar).grid(row=4, column=1)
paymentmodeentry = Entry(root, textvariable=paymentmodevar).grid(row=5, column=1)

# Check Box
Checkbutton(root, text="Do you want meals", variable=checkboxvar,font="comicsansms 15 bold").grid(row=6, column=1)

#Sumit Button
Button(root, text="Sumit",font="comicsansms 15 bold", command=store).grid(row=7, column=1)

root.mainloop()