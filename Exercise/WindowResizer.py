from tkinter import *

root = Tk()
root.title("Window Generator")

def NewGUI():
    root = Tk()

    root.title("New Window")
    canvas_width = widthvar.get()
    canvas_height = heightvar.get()
    root.geometry(f"{canvas_width}x{canvas_height}")
    Label(root, text="This is Your desire Window").pack(pady=25)

    root.mainloop()

canvas_width = 500
canvas_height = 150
root.geometry(f"{canvas_width}x{canvas_height}")

Label(root, text="Welcome to Window Resizer", font="comicsansms 20 bold").grid(row=0, column=1)

Width = Label(root, text="Width").grid(row=3, column=0)
Height = Label(root, text="Height").grid(row=4, column=0)

widthvar = IntVar()
heightvar = IntVar()

widthentry = Entry(root, textvariable=widthvar).grid(row=3, column=1)
heightentry = Entry(root, textvariable=heightvar).grid(row=4, column=1)

Button(root, text="Sumit", command = NewGUI).grid(row=5, column=1)

root.mainloop()