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
widget.bind("<Double-1>", quit)# On double click coordinates function executed
widget.bind("Motion", coordinates)
root.mainloop()