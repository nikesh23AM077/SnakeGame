from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        # with open("data.txt") as data:
        #     self.high_score=int(data.read())
        with open("data.txt") as data:
            content = data.read().strip()
            self.high_score = int(content) if content else 0

        
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_score()
        self.hideturtle()
    

    def reset(self):
        if self.score > self.high_score:
            self.high_score= self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER",align="center",font=("Arial","24","normal"))
    

    def update_score(self):
        self.clear()
        self.write(f"SCORE:{self.score} HIGH SCORE {self.high_score}",align="center",font=("Arial","24","normal"))


    def increase_score(self):
        self.score+=1
        
        self.update_score()