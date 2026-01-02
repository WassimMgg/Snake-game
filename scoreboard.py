from turtle import Turtle
FONT = ('Courier', 14, 'normal')
ALIGNEMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ur_score = 0
        with open("data.txt") as file:
            content = int(file.read())
        self.high_score = content
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,290)
        self.write(f"Score: {self.ur_score}  High Score: {self.high_score}", align = ALIGNEMENT, font = FONT)
    
    def update_score(self):
        self.clear()
        self.ur_score += 1
        self.write(f"Score: {self.ur_score}  High Score: {self.high_score}", align = ALIGNEMENT, font = FONT)
        
        

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over.", align = ALIGNEMENT, font = FONT)

    def reset(self):
        if self.ur_score > self.high_score:
            self.high_score = self.ur_score
            with open("data.txt", mode = "w") as file:
                file.write(f"{self.high_score}")
        self.ur_score = 0
        self.clear()
        self.write(f"Score: {self.ur_score}  High Score: {self.high_score}", align = ALIGNEMENT, font = FONT)