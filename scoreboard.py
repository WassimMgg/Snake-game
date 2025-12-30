from turtle import Turtle
FONT = ('Courier', 14, 'normal')
ALIGNEMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ur_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,290)
        self.write(f"Score: {self.ur_score}", align = ALIGNEMENT, font = FONT)
    
    def update_score(self):
        self.clear()
        self.ur_score += 1
        self.write(f"Score: {self.ur_score}", align = ALIGNEMENT, font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.", align = ALIGNEMENT, font = FONT)