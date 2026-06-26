from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(0,260)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
            self.score += 1
            self.clear()
            self.update_scoreboard()

    def start_message(self):
        self.clear()
        self.goto(0,0)
        self.write("PRESS SPACE TO START", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center",
                   font=("Courier", 24, "normal"))


    def pause_message(self):
        self.goto(0,0)
        self.write("PAUSED", align=ALIGNMENT, font=FONT)


    def reset(self):
        self.clear()
        self.score = 0
        self.goto(0,0)
        self.update_scoreboard()