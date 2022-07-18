# Radio Button
from tkinter import *
import tkinter.messagebox as mb

root = Tk()
root.geometry("630x467")
root.title("Raidio Button")

def order():
	"""This function will show message box"""
	mb.showinfo("Order Received", f"Your have ordered: {var.get()}")

Label(root,text = "What do you like?", font = "lucika 16 bold").pack()

var = StringVar()
#var.set("Jalebi")

#Radio buttons
radio = Radiobutton(root, text = "Jalebi", variable = var, value = "Jalebi", pady = 16)
radio.pack(side=TOP, anchor = "nw")

radio2 = Radiobutton(root, text = "Samosa", variable = var, value = "Samosa", pady = 16)
radio2.pack(anchor = "nw")

radio3 = Radiobutton(root, text = "Rabri", variable = var, value="Rabri", pady = 16)
radio3.pack(anchor = "nw")

radio4 = Radiobutton(root, text = "Litti", variable = var, value ="Litti",pady = 16)
radio4.pack(anchor = "nw")

radio5 = Radiobutton(root, text = "kaju Barfi", variable =var, value="Kaju Barfi",pady = 16)
radio5.pack(anchor = "nw")

# Order Now Button
Button(root, text = "Order Now", command = order).pack()

root.mainloop()
