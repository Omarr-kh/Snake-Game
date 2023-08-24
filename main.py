from snake import Snake
from turtle import Screen
from scoreboard import Score
import time
from food import Food

GAME_ON = True

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
while GAME_ON:
    screen.update()
    time.sleep(0.1)
    snake.move()

    for segment in snake.body_segments[1:]:
        if snake.head.distance(segment) < 10:
            # GAME_ON = False
            score.game_over()
            snake.destroy_snake()

    # check for collisions with the walls
    if snake.head.xcor() < -295 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 295:
        # GAME_ON = False
        score.game_over()
        snake.destroy_snake()

    if snake.head.distance(food) < 15:
        snake.add_segment()
        score.update_score()
        food.create_food()

screen.exitonclick()
