from turtle import Screen
from snake import Snake
from time import sleep

screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
# Turn off tracer (animation while turtle is moving):
screen.tracer(0)

snake = Snake()

game_on = True
while game_on:
    # refresh the screen each time, and after 0.2 delay:
    screen.update()
    sleep(0.2)

    snake.move()


screen.exitonclick()

