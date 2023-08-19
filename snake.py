import turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self) -> None:
        self.body_segments = []
        self.create_snake()
        self.head = self.body_segments[0]


    def create_snake(self):
        for pos in STARTING_POSITIONS:
            trtle = turtle.Turtle("square")
            trtle.penup()
            if pos == (0, 0):
                trtle.color("red")
            else:
                trtle.color("white")
            trtle.goto(pos)
            self.body_segments.append(trtle)


    def move(self):
        for i in range(len(self.body_segments) - 1, 0, -1):
            prev_x = self.body_segments[i - 1].xcor()
            prev_y = self.body_segments[i - 1].ycor()
            self.body_segments[i].goto(prev_x, prev_y)
        self.head.forward(20)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
