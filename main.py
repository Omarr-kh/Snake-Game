from snake import Snake
from turtle import Screen
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
