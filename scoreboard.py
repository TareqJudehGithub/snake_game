# scoreboard class that inherits from Turtle() class.
from turtle import Turtle
from time import sleep

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=275)
        self.hideturtle()
        self.update_scoreboard()

    # Displaying and updating the score:
    def update_scoreboard(self):
        self.clear()
        self.color("white")
        self.goto(x=0, y=275)
        self.write(f"Score: {self.score}   High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 100)
        self.color("red")
        self.write("Game Over", align=ALIGNMENT, font=("Courier", 20, "bold"))
        sleep(3)
        self.clear()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()





