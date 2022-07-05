from tkinter import *

root = Tk()

root.geometry("700x433")
root.title("Text Styling")
#Important Labels:
# text = adds the text
# bg = Background
# fg = foreground
# font = sets font style, size, Structure
# 1. font = ("comicsansms", 34, "bold")
# 2. font = "comicsansms 34 bold"
# padx = x-_Padding
# pady = y - _Padding
# 1.padx = 34
# 2.pady = 3
# 1.padx = "34px"
# 2.pady = "3px"
# borderwidth = create width of border
# relief = create border styling = SUNKEN, RAISED, GROOVE, RIDGE

sample = Label(text="activebackground, activeforeground, anchor, background, bitmap,\nborderwidth, cursor, disabledforeground, font, foreground,\nhighlightbackground, highlightcolor, highlightthickness, image\njustify, padx, pady, relief, takefocus, text,\ntextvariable, underline, wraplength", bg = "red", fg= "white", pady=150, padx=20, font=("comicsansms", 10, "bold"), borderwidth=3, relief=RIDGE)

# Impotant Pack options
# anchor = ne
# side = TOP,BOTTOM,LEFT,RIGHT
# padx = x margin
# pady = y margin
# sample.pack(side = TOP, anchor="nw", fill = X) #not going down without using side
sample.pack(side = TOP,fill = Y, padx=34 , pady=34)
root.mainloop()