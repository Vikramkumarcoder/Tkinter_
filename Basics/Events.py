from tkinter import *


root = Tk()
root.title("Events Handling")
root.geometry("340x388")


def coordinates(event):
    print(f"Button is at {event.x},{event.y}")

widget = Button(root, text="Click")
widget.pack()

"""the event <Button-1>, the middle button by <Button-2>, and the rightmost mouse button by <Button-3>.
   <Button-4> defines the scroll up event on mice with wheel support and and <Button-5> the scroll down.
   You can use ButtonPress instead of Button, or even leave it out completely: , , and <1> are all synonyms."""
widget.bind("<Button-1>", coordinates) # On one click coordinates function executed

"""Similar to the Button event, see above, but the button is double clicked instead of a single click. To specify the left, middle or right   
   mouse button use <Double-Button-1>, <Double-Button-2>, and <Double-Button-3> respectively.
   You can use Double or Triple as prefixes. Note that if you bind to both a single click (<Button-1>) and a double click 
   (<Double-Button-1>), both bindings will be called."""
widget.bind("<Double-1>", quit)# On double click coordinates function executed

"""The mouse is moved with a mouse button being held down. To specify the left, middle or right mouse button use <B1-Motion>, <B2-Motion> and
   <B3-Motion> respectively. The current position of the mouse pointer is provided in the x and y members of the event object passed to the 
   callback, i.e. event.x, event.y"""
widget.bind("Motion", coordinates)


root.mainloop()