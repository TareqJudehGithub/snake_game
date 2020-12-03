from turtle import Turtle
from random import randint
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # circle default size is 20*20, but we want it displayed as 10*10:
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = randint(-270, 270)
        random_y = randint(-270, 270)
        self.goto(random_x, random_y)

