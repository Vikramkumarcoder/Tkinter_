from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('300x200')


frame = Frame(ws, bg='#ccffcc')
frame.pack()

food = LabelFrame(frame, text='Food', bd=5, relief=RIDGE)

food.grid(row=0, column=0, sticky=W, padx=20, pady=20)

Checkbutton(food, text='Pizza').pack(anchor=W)
Checkbutton(food, text='Noodles').pack(anchor=W)

ws.mainloop ()