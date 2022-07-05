from msilib.schema import File
from tkinter import *
import tkinter

root = Tk()
root.geometry("600x389")
def BrandName():
    print("VikramCoder")
def Estabilised():
    print(1997)
def NetWorth():
    print("$"+"200"+" Million")
def Field():
    print("Technology")
root.title("BUTTON")

b1 = Button(bg="grey", text=" X ", fg="red", command=root.destroy)
b1.pack(side=RIGHT,anchor="ne", padx=10)
f1 = Frame(root)
f1.pack()
b1 = Button(f1, bg="grey", text="Brand Name", fg="white", command=BrandName)
b1.pack(side=LEFT, padx=25 , pady=40)
b1 = Button(f1, bg="grey", text="   Sector   ", fg="white", command=Field)
b1.pack(side=LEFT,padx=25)
b1 = Button(f1, bg="grey", text="   Since   ", fg="white", command=Estabilised)
b1.pack(side=LEFT,padx=25)
b1 = Button(f1, bg="grey", text="Net Worth", fg="white", command=NetWorth)
b1.pack(side=LEFT,padx=25)

root.mainloop()