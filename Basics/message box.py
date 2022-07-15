#pylint:disable=W0105
#pylint:disable=W0401
from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root. title("Menu")
root. geometry ("649x563")
def func():
    Label(text="hello"). pack()
    
def helping():
	Label(text = "How can i help you?").pack()
	#This will show message box
	tmsg.showinfo("Experience", "We will soon help you.")
	
def rate():
	# Use to ask questions in "yes" or "no" form.
	ans = tmsg.askquestion("Experience", "Do you like my application?")
	if ans == "yes":
		tmsg.showinfo("Reply", "Great, Please rate us in Play store")
	elif ans == "no":
		tmsg.showinfo("Reply", "Tell us what went wrong")
		
def service():
	"""This will return 1 if "retry" clicked or 0 if "cancel" clicked"""
	ans = tmsg.askretrycancel("sever", "Sever error")
	if ans:
		tmsg.showinfo("Reply", "Congratulation! You won $1000000")
	elif not ans:
		tmsg.showinfo("Reply", "If you had  clicked on retry,\nthen you could won prize")
		
def terms():
	tmsg.askyesnocancel("T&C", "Do you read our terms and conditions")

#File Menus and their submenus
mainfile = Menu(root)
m1 = Menu(mainfile, tearoff = 1)
m1.add_command(label = "New Project", command = func)
m1.add_command(label = "save", command = func)
m1.add_separator()#for separation line between two submenus
m1.add_command(label = "save as", command = func)
m1.add_command(label = "Print", command = func)
root.config(menu = mainfile)
mainfile.add_cascade(label = "File", menu = m1)


# Edit menu and their submenus
m2 = Menu(mainfile, tearoff = 0)
m2.add_command(label = "Copy", command = func)
m2.add_command(label = "Paste", command = func)
m2.add_command(label = "Insert", command = func)
m2.add_command(label = "Cut", command = func)
mainfile.add_cascade(label = "Edit", menu = m2)

# Help menu
m3 = Menu(mainfile)
m3.add_command(label = "help", command = helping)
m3.add_command(label = "Rate us", command = rate)
m3.add_command(label = "Service", command = service)
m3.add_command(label = "T&C", command = terms)
mainfile.add_cascade(label = "Help", menu = m3)
mainfile.config()

root. mainloop()