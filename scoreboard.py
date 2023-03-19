from turtle import Turtle
ALIGNMENT = "Center"
FONT = ("Arial", 16, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.pendown()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
