from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.score = 0
        self.write(f"Score: {self.score}", align="center")
        
        

    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.write(f"Score: {self.score}", align="center")
        
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center")
   
