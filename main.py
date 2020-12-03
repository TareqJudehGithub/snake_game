from turtle import Screen, distance
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
# Turn off tracer (animation while turtle is moving):
screen.tracer(0)

# Instances:
snake = Snake()
food = Food()
score = Scoreboard()

# Key listening events:
screen.listen()
screen.onkey(snake.direction_up, "Up")
screen.onkey(snake.direction_down, "Down")
screen.onkey(snake.direction_right, "Right")
screen.onkey(snake.direction_left, "Left")


game_on = True
while game_on:
    # refresh the screen each time, and after 0.2 delay:
    screen.update()
    sleep(0.1)
    snake.move()

    # Detect collision with food:
    # Distance from snake head to the food:
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()

screen.exitonclick()

