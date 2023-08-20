import turtle
import random

class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.shape("circle")
        self.penup()
        self.create_food()


    def create_food(self):
        x_pos = random.randint(-280, 280)
        y_pos = random.randint(-280, 280)
        self.goto(x_pos, y_pos)
