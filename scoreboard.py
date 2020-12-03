# scoreboard class that inherits from Turtle() class.
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=275)
        self.hideturtle()
        self.update_scoreboard()

    # Displaying and updating the score:
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT
        )


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()





