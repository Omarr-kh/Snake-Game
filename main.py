from snake import Snake
from turtle import Screen
from scoreboard import Score
import time
from food import Food

# Creating the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake")

snake = Snake()
food = Food()
score = Score()

# Creating event listeners for snake movements
screen.listen()
screen.onkeypress(snake.up, 'Up')
screen.onkeypress(snake.down, 'Down')
screen.onkeypress(snake.right, 'Right')
screen.onkeypress(snake.left, 'Left')

# Game loop
while True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        score.update_score()
        food.create_food()
