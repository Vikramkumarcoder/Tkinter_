#pylint:disable=W0401
#Sliders

from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("630x389")
root.title("Slider")

def get():
	"""This will generate messagebox"""
	tmsg.showinfo("Winner", f"You are eligible for ${horslider.get()}")

#Verticle Slider
#verslider = Scale(root, from_ = 0, to=100)
#verslider.pack()

Label(root, text = "How much money do you want?").pack()

#Horizontal Slider
horslider = Scale(root, from_ = 0, to = 5, orient = HORIZONTAL, tickinterval = 1)
horslider.pack()

horslider.set(2.5)#It set initial value of slider

#Get Button
Button(root, text = "   Get   ", command = get).pack(pady = 20)

root.mainloop()