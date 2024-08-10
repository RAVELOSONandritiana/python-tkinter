from tkinter import *
from random import choice
def art(fen,can):
    for element in can.find_all():
        can.delete(element)
    rayon = 20
    taille = 400
    color = ['#FF0007','#D058D0','#FFFF00','#15FF00','#FFFFFF','#1A1212','#FF6D00','#2222DF']
    for ligne in range(0,taille,int(taille/rayon)):
        for colonne in range(0,taille,int(taille/rayon)):
            x1 = ligne
            y1 = colonne
            x2 = ligne + rayon
            y2 = colonne + rayon
            can.create_rectangle(x1,y1,x2,y2,fill=choice(color))
            if(choice([0,1,2]) == 0):
                can.create_oval(x1+5,y1+5,x2-5,y2-5,fill=choice(color))
            elif (choice([0,1,2]) == 1):
                can.create_rectangle(x1+5,y1+5,x2-5,y2-5,fill=choice(color))
            elif (choice([0,1,2]) == 2):
                can.create_arc(x1+5,y1+5,x2-5,y2-5,fill=choice(color),start=0,extent=choice(range(0,360,10)))
fen = Tk()
can = Canvas(height=400,width=400,bg="grey")
art(fen,can)
can.pack()
def d(event):
    art(fen,can)
fen.bind_all("<Key-r>",d)
fen.mainloop()