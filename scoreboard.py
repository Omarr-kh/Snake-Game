import turtle


class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        with open("highscore.txt", "r") as f:
            self.highscore = int(f.read())
        self.show_score()

    def show_score(self):
        self.goto(0, 270)
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align="center",
                font=('Arial', 18, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def game_over(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("./highscore.txt", "w") as f:
                f.write(str(self.highscore))
        self.score = 0
        self.clear()
        self.show_score()
        # self.goto(0, 0)
        # self.write("GAME OVER!", align="center",
        #         font=('Arial', 18, 'normal'))
