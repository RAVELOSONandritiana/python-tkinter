from tkinter import *
from modules import *
import sys
def reload(event):
    global can,fen,HEIGHT,WIDTH,tour,index_green,index_red,player
    index_green = []
    index_red = []
    tour = 0
    animate(fen,can,HEIGHT,WIDTH,['black','gray'])
    create_plateau(fen,can,HEIGHT,WIDTH)

def reloa(color):
    global can,fen,HEIGHT,WIDTH,tour,index_green,index_red
    index_green = []
    index_red = []
    tour = 0
    animate(fen,can,HEIGHT,WIDTH,color)
    create_plateau(fen,can,HEIGHT,WIDTH)

def addOval(event):
    global can,fen,tour,index_red,index_green
    r = 3
    color_oval = ['#FF0100' , '#48F814']
    objet_proche = can.find_closest(event.x,event.y)
    tag = can.itemcget(objet_proche,'tag').split(' ')[0]
    if tag == "terrain":
        x1,y1,x2,y2 = can.coords(objet_proche)
        oval = can.create_oval(x1+r,y1+r,x2-r,y2-r,fill=color_oval[tour])
        
        if tour == 0:
            index_red.append(can.coords(oval))
            col = detect(index_red)
            if col == "gagne":
                reloa(['blue','red'])
                tour-=1
        else:
            index_green.append(can.coords(oval))
            col = detect(index_green)
            if col == "gagne":
                reloa(['black','green'])
                tour-=1
        tour+=1
        fen.title(player[tour%2])
        tour = tour%2

def detect(index_red):
    global N
    if len(index_red) >= N:
        # tri vertical
        index_red.sort(key=lambda x:x[3])
        for index,element in enumerate(index_red):
            cpt = 1
            x = element[0]
            y = element[3]
            for j in index_red[index:]:
                if j[3] == y+20 and j[0] == x:
                    cpt+=1
                    y = j[3]
                if cpt == N:
                    return "gagne"
        #tri horizontal
        index_red.sort(key=lambda x:x[0])
        for index,element in enumerate(index_red):
            cpt = 1
            x = element[0]
            y = element[3]
            for j in index_red[index:]:
                if j[0] == x+20 and j[3] == y:
                    cpt+=1
                    x = j[0]
                if cpt == N:
                    return "gagne"
        #tri oblique vers haut
        index_red.sort(key=lambda x:x[0])
        for index,element in enumerate(index_red):
            cpt = 1
            x = element[0]
            y1 = element[1]
            for j in index_red[index:]:
                if j[0] == x+20 and j[1] == y1-20:
                    x = j[0]
                    y1 = j[1]
                    cpt+=1
                    if cpt == N:
                        return "gagne"
        # tri oblique vers bas
        index_red.sort(key=lambda x:x[0])
        for index,element in enumerate(index_red):
            cpt = 1
            x = element[0]
            y1 = element[1]
            for j in index_red[index:]:
                if j[0] == x+20 and j[1] == y1+20:
                    x = j[0]
                    y1 = j[1]
                    cpt+=1
                    if cpt == N:
                        return "gagne"

HEIGHT = 602
WIDTH = 602
tour = 0
N = 5   #nombre d'element a algne pour gagner
index_red = []
index_green = []
player = ['red' , 'green']
fen = Tk()
can = Canvas(height=HEIGHT,width=WIDTH,bg="gray")
can.pack()
animate(fen,can,HEIGHT,WIDTH,['black','white','gray'])
liste_mine = create_plateau(fen,can,HEIGHT,WIDTH)

can.bind_all("<Button-1>",addOval)
can.bind_all("<Key-r>",reload)
fen.title(player[tour%2])
fen.mainloop()