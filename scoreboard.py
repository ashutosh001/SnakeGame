from turtle import Turtle
ALIGNMENT = "center"
FONT =  ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_score()
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
        self.write(f"Score : {self.score}, High Score : {self.high_score}",align=ALIGNMENT,font=FONT)

    def reset_scoreboard(self):
        """Calculates the high score, then resets the scoreboard"""
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()
        self.write_score()

    def write_score(self):
        """Writes the high score to a file"""
        with open("high_score.txt","w") as file:
            file.write(str(self.high_score))

    def read_score(self):
        """Reads the high score from the file"""
        with open("high_score.txt") as file:
            high_score = int(file.read())
        return high_score