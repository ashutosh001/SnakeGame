from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.up()
        self.goto(0,250)
        self.write(f"Score : {self.score}",align="center",font=("Arial", 24, "normal"))

    def update_score(self):
        """Increases the score by one and updates the scoreboard"""
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}",align="center",font=("Arial", 24, "normal"))