from tkinter import *

root = Tk()
root. title("Menu")
root. geometry ("649x563")
def func():
    Label(text="hello"). pack()

"""use it for non-dropdown menu"""

#mymenu = Menu(root)
#mymenu. add_command(label = "Menu", command = func)
#mymenu. add_command(label = "Exit", command = quit)
#root.config(menu = mymenu)

"""Use it for drop-down menu"""

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


root. mainloop()
