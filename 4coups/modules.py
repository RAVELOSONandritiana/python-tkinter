from random import shuffle,choice
def create_plateau(fen,can,HEIGHT,WIDTH):
    for element in can.find_all():
        can.delete(element)
    w = 20
    for ligne in range(1,HEIGHT,w):
        for colonne in range(1,WIDTH,w):
            x1 = ligne
            y1 = colonne
            x2 = x1 + w
            y2 = y1 + w
            can.create_rectangle(x1,y1,x2,y2,fill="black",outline="blue",tag="terrain")

tour = 0
def animate(fen,can,HEIGHT,WIDTH,color):
    global tour
    for element in can.find_all():
        can.delete(element)
    w = 40
    for ligne in range(tour*10,HEIGHT-tour*10,w):
        for colonne in range(tour*10,WIDTH-tour*10,w):
            x1 = ligne
            y1 = colonne
            x2 = x1 + w
            y2 = y1 + w
            can.create_rectangle(x1,y1,x2,y2,fill=choice(color),outline="blue")
    tour+=1
    if tour != 100:
        can.after(20,animate,fen,can,HEIGHT,WIDTH,color)
    else:
        tour = 0
        create_plateau(fen,can,HEIGHT,WIDTH)
