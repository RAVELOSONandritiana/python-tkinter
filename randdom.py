from tkinter import *
import random
def construct_(fen,canvas):
    elements = canvas.find_all()
    for element in elements:
        canvas.delete(element)
    color = ['white','black','blue']
    for ligne in range(0,400,20):
        for colonne in range(0,400,20):
            x1 = ligne
            y1 = colonne
            x2 = x1+20
            y2 = y1+20
            canvas.create_rectangle(x1,y1,x2,y2,fill=random.choice(color))
    fen.after(20,construct_,fen,canvas)

fen = Tk()
can = Canvas(height=400,width=400,bg="grey")
construct_(fen,can)
    
can.pack()
fen.title("animation")
fen.mainloop()
