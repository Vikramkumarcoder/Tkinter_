# List Box

from tkinter import *

root = Tk()
root.geometry("460x367")
root.title("List Box")

def add():
	global num
	lbx.insert(ACTIVE, num)
	num+=1

num = 0
lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First Inserted sample text")

Button(root, text = "ADD", command = add).pack()

root.mainloop()
