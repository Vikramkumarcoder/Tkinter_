from tkinter import *

root = Tk()
root.geometry("550x280")
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
Label(root, text="Welcome to Vikram Airline", font="comicsansms 20 bold", pady=10).grid(row=0, column=3)

# Text LABELING AND GRIDING
name = Label(root, text="Name", font="comicsansms 10 bold").grid(row=1, column=2)
phone = Label(root, text="Phone", font="comicsansms 10 bold").grid(row=2, column=2)
gender = Label(root, text="Gender", font="comicsansms 10 bold").grid(row=3, column=2)
emergency = Label(root, text="Emergency contacts", font="comicsansms 10 bold").grid(row=4, column=2)
paymentmode = Label(root, text="Payment Mode", font="comicsansms 10 bold").grid(row=5, column=2)

# Entry variables of respective texts
namevar = StringVar()
phonevar = StringVar()
gendervar = StringVar()
emergencyvar = StringVar()
paymentmodevar = StringVar()
checkboxvar = IntVar()

# Entries and pack with grid
nameentry = Entry(root, textvariable=namevar).grid(row=1, column=3)
pnoneentry = Entry(root, textvariable=phonevar).grid(row=2, column=3)
genderentry = Entry(root,textvariable=gendervar).grid(row=3, column=3)
emergencyentry = Entry(root, textvariable=emergencyvar).grid(row=4, column=3)
paymentmodeentry = Entry(root, textvariable=paymentmodevar).grid(row=5, column=3)

# Check Box
Checkbutton(root, text="Do you want meals", variable=checkboxvar,font="comicsansms 15 bold").grid(row=6, column=3)

#Sumit Button
Button(root, text="Sumit",font="comicsansms 15 bold", command=store).grid(row=7, column=3)

root.mainloop()