from turtle import Screen
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

    # Detect collision with food and with wall:
    if snake.head.distance(food) < 15:
        # respawn food in a new random location:
        food.refresh()
        # add more segment to Snake:
        snake.extend()
        # Update Score:
        score.increase_score()

    # Detect collision with wall and with wall:
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        score.reset()
        score.game_over()
        food.refresh()
        snake.reset()

    # Detect collision with Snake body:
    for segment in snake.segments[1::]:
        if snake.head.distance(segment) < 10:
            score.reset()
            score.game_over()
            food.refresh()
            snake.reset()


screen.exitonclick()

