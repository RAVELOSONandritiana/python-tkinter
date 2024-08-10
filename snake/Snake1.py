from random import choice
from math import sqrt
class Snake1(object):
    def __init__(self,fen,can):
        self.fen = fen
        self.can = can
        self.rayon = 6
        self.dir_dict = {
            "up":[0,-self.rayon*2],
            "down":[0,self.rayon*2],
            "left":[-self.rayon*2,0],
            "right":[self.rayon*2,0]
        }
        self.color_snake = choice(['red','yellow','black'])
        self.coords_fruit = []
        self.createFruit()
        self.coords_snake = []
        self.direction = "right"
        self.status = 0
        self.createOval()
        self.can.bind_all('<KeyPress>',self.change_dir)
        self.animSnake()

    def createOval(self):
        x = choice(range(102,200,self.rayon*2))
        y = choice(range(102,200,self.rayon*2))
        for i in range(4):
            corps = self.can.create_rectangle(x-self.rayon-i*self.rayon*2,y-self.rayon,x+self.rayon-i*self.rayon*2,y+self.rayon,fill=self.color_snake,outline=self.color_snake,tag="tete" if i == 0 else "corps")
            self.coords_snake.append(self.can.coords(corps))

    def show(self):
        self.fen.mainloop()

    def change_dir(self,event):
        key = event.keysym
        if self.status:
            if key == "Left" and self.direction != 'right':
                self.direction = "left"
            elif key == "Up" and self.direction != 'down':
                self.direction = "up"
            elif key == "Right" and self.direction != 'left':
                self.direction = "right"
            elif key == "Down" and self.direction != 'up':
                self.direction = "down"
        if key == "space":
            self.status += 1
            self.status %= 2

    def animSnake(self):
        x,y = self.dir_dict[self.direction]
        debut = self.coords_snake[0]
        fin = self.coords_snake[-1]
        devant = 0
        col = 0
        if self.status:
            for tete in self.can.find_withtag('tete'):
                self.can.move(tete,x,y)
                d = self.collision(self.can.coords(tete),self.coords_fruit)
                if d == 0:
                    self.can.delete(*self.can.find_withtag('fruit'))
                    self.createFruit()
                    col = 1
            for corps in self.can.find_withtag('corps'):
                self.can.coords(corps,self.coords_snake[devant])
                devant+=1
        self.coords_snake = []
        for i in self.can.find_withtag('tete'):
            self.coords_snake.append(self.can.coords(i))
            for i in self.can.find_withtag('corps'):
                self.coords_snake.append(self.can.coords(i))
        if col == 1:
            corps = self.can.create_rectangle(fin,fill=self.color_snake,outline=self.color_snake,tag="corps")
            self.coords_snake.append(self.can.coords(corps))
        for i in self.can.find_withtag('corps'):
            d = self.collision(self.can.coords(*self.can.find_withtag('tete')),self.can.coords(i))
            if d == 0:
                self.status = 0
        self.can.after(100,self.animSnake)

    def createFruit(self):
        for fruit in self.can.find_withtag('fruit'):
            self.can.delete(fruit)
        x = choice(range(0+self.rayon,401,self.rayon*2))
        y = choice(range(0+self.rayon,401,self.rayon*2))
        fruit = self.can.create_rectangle(x-self.rayon,y-self.rayon,x+self.rayon,y+self.rayon,fill="blue",tag="fruit")
        for i in list(self.can.find_withtag('corps'))+list(self.can.find_withtag('tete')):
            d = self.collision(self.can.coords(fruit),self.can.coords(i))
            if d == 0:
                self.createFruit()
        self.coords_fruit = self.can.coords(fruit)

    def collision(self,a,b):
        if len(a) == 4 and len(b) == 4:
            x1,y1 = a[0]+self.rayon,a[1]+self.rayon
            x2,y2 = b[0]+self.rayon,b[1]+self.rayon
            d = sqrt((x2-x1)**2+(y2-y1)**2)
            for element in self.can.find_withtag('tete'):
                x1,y1,x2,y2 = self.can.coords(element)
                if x1 < 0 or y1 < 0 or x2 > int(self.can.cget('width')) or y2 > int(self.can.cget('height')):
                    self.status = 0
            return d
