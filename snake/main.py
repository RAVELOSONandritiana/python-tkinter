from tkinter import *
import Snake
WIDTH = 400
HEIGHT= 400
fen = Tk()
fen.geometry(f"{WIDTH}x{HEIGHT}+1000+0")
fen.title("Snake game")
can = Canvas(width=WIDTH,height=HEIGHT,bg="grey")
can.pack()

snake = Snake.Snake1(fen,can)
snake.show()

fen.mainloop()

