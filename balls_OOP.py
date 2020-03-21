from tkinter import *
from random import randint

WIDTH = 800
HEIGHT = 500
OUR_COLOR = ["red","green","yellow","orange","blue","indigo","black"]  # список возможных цветов


class Ball:
    def __init__(self):

        self.R = randint(10, 50)
        self.x = randint(self.R, WIDTH - self.R)
        self.y = randint(self.R, HEIGHT - self.R)

        self.dx, self.dy = (+randint(1,10), + randint(1,10))      # скорость будет случаной

        self.ball_id = canvas.create_oval(self.x - self.R,
                                          self.y - self.R,
                                          self.x + self.R,
                                          self.y + self.R,
                                          fill=OUR_COLOR[randint(0,len(OUR_COLOR)-1)])  # цвет всегда будет рандомным

    def move(self):

        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0:
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or self.y - self.R <= 0:
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


def canvas_click_handler (event):
    print('Hello World! x=', event.x, 'y=', event.y)


def tick():
    for ball in balls:  # обеспечение движения и отображения каждому шару
        ball.move()
        ball.show()

    root.after(50, tick)


def main():
    global root, canvas, balls
    root = Tk()
    root.geometry(str(WIDTH)+"x"+str(HEIGHT))

    canvas = Canvas(root)
    canvas.config(width=WIDTH,height=HEIGHT)
    canvas.pack(fill=BOTH)
    canvas.bind("<Button-1>",canvas_click_handler)

    balls = [Ball() for ball in range(100)]  # создаем список шаров
    tick()

    root.mainloop()


if __name__ == '__main__':
    main()
