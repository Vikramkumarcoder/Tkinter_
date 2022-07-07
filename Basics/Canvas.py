from tkinter import *

root = Tk()
root.title("Canvas")

canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")

can_widget = Canvas(root, width = canvas_width,height = canvas_height, bg="SpringGreen2")
can_widget.pack()

# Drawing line parameters: x1, y1 , x2, y2
can_widget.create_line(0, 0, 800, 400)
can_widget.create_line(0, 400, 800, 0)

# Drawing rectangle parameters: x1, y1 , x2, y2 which is the coordinates of two opposite vertices
can_widget.create_rectangle(0, 200, 600, 0, fill="red")

#Drawing Oval parameters: x1, y1 , x2, y2 which is the coordinates of two opposite vertices in which oval can draw
can_widget.create_oval(0, 200, 600, 0, fill="black")

"""Create arc shaped region with coordinates x1,y1,x2,y2."""
can_widget.create_arc(0, 300, 700, 300)

"""Create polygon with coordinates x1,y1,...,xn,yn."""
can_widget.create_polygon(100, 100, 300, 100, 400, 300, 300, 500, 100, 300, fill="blue")


"""Create text with coordinates x1,y1."""
can_widget.create_text(390, 200, text="This is sample text", fill="purple", font=("Helvetica 35 bold"))


root.mainloop()