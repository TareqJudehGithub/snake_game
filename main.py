from turtle import Turtle, Screen
from time import sleep

screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
# Turn animation off:
screen.tracer(0)


# Creating a starting position for the snake:
start_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

# Creating a snake body:
for position in start_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

screen.update()

game_on = True
while game_on:
    screen.update()
    sleep(0.1)

    # Last to first:
    for seg_num in range(len(segments) - 1, 0, - 1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].right(90)











screen.exitonclick()

