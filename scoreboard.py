import turtle


class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.show_score()

    def show_score(self):
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center",
                font=('Arial', 18, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center",
                font=('Arial', 18, 'normal'))
