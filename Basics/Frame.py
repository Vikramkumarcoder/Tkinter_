from tkinter import *

root = Tk()
root.geometry("800x700")
root.title("Frame")
f1 = Frame(root, bg = "grey", borderwidth=6 , relief=RAISED, padx=33)
f1.pack(side= LEFT, fill=Y)
f2 = Frame(root, bg="grey", border=6, relief=RAISED)
f2.pack(side=TOP, fill=X)
l1 = Label(f1, text="This is VS code UI", font=("Comic Sans Ms", 20, "bold"))
l1.pack(pady=320)
l2 = Label(f2, text="Welcome to VS Code!", font=("Comic Sans Ms", 20, "bold"), fg="red")
l2.pack()
root.mainloop()