from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    # Creating a starting position for the snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Creating a snake body:
    def create_snake(self):
        for position in START_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # Add a new segment to the position of the last segment in Snake:
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, - 1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def direction_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def direction_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def direction_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def direction_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
