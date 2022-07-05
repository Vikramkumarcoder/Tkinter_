from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("The Times Of India")
root.geometry("600x500")
# root.maxsize(900,20000)
name = "THE TIMES OF INDIA"
images1 = Image.open("news1.png")
image1 = ImageTk.PhotoImage(images1)
# image1 = PhotoImage(file = "news.png")
image2 = "Image2"
image3 = "Image3"
image4 = "Image4"
image5 = "Image5"
text1 = """


In 1555, before her accession to the throne, a teenage Elizabeth the Great of England was imprisoned on suspicion of \ntreason. In Woodstock castle, she used a diamond ring to scratch on a glass pane the words: “Much suspected of me. Nothing proved can be”.
The recent Supreme Court judgment in Zakia Jafris case which upheld the exoneration of the then chief minister and other officials \nof Gujarat, in respect of a criminal conspiracy concerning the 2002 violence in Gujarat similarly holds: “…absent clear and \ndirect material indicative of involvement of named person(s) in hatching criminal conspiracy to cause mass violence across the \nState targeting minority community during the relevant period, the attempt of the appellant, if we may say so, is bordering on \nsewing of insignificant unconnected circumstances and events regarding the failures and in some cases, laxity in administration, \nwhich is being projected as an act of concerted effort of all the State officials up to the highest level without there being any \ntittle of material to show that there was meeting of minds of all these persons at some level.”"""
text2 = "Text2"
text3 = "Text3"
text4 = "Text4"
text5 = "Text5"
title = Label(text=name,border = 2, relief= RAISED, padx=40 , pady=20, font=("Times New Roman", 100, "normal") )
photo1 = Label(image=image1, bg="grey", border = 2, relief= RAISED, padx=20 , pady=10)
photo2 = Label(text=image2, bg="grey", border = 5, relief= RAISED, padx=40 , pady=20)
photo3 = Label(text=image3, bg="grey", border = 5, relief= RAISED, padx=40 , pady=20)
photo4 = Label(text=image4, bg="grey", border = 5, relief= RAISED, padx=40 , pady=20)
photo5 = Label(text=image5, bg="grey", border = 5, relief= RAISED, padx=40 , pady=20)
words1 = Label(text=text1, border = 2, relief= RAISED, padx=40 , pady=20,font=("Times New Roman", 15, "bold"))
words2 = Label(text=text2, bg="grey", border = 5, relief= RAISED, padx=40 , pady=20)
words3 = Label(text=text3, bg="grey", border = 5, relief= RAISED, padx=40 , pady=20)
words4 = Label(text=text4, bg="grey", border = 5, relief= RAISED, padx=40 , pady=20)
words5 = Label(text=text5, bg="grey", border = 5, relief= RAISED, padx=40 , pady=20)
title.pack(fill=X,padx=20)
photo1.pack(side=TOP)
words1.pack(side=TOP)
photo2.pack()
words2.pack()
photo3.pack()
words3.pack()
photo4.pack()
words4.pack()
photo5.pack()
words5.pack()

root.mainloop()