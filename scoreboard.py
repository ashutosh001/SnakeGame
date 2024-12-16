from turtle import Turtle
ALIGNMENT = "center"
FONT =  ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.up()
        self.goto(0,265)
        self.update_score()
    
    def increase_score(self):
        """Increases the Score by one"""
        self.score +=1
        self.update_score()

    def update_score(self):
        """Updates the scoreboard"""
        self.clear()
        self.write(f"Score : {self.score}",align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align=ALIGNMENT,font=FONT)