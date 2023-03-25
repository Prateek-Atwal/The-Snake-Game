from turtle import Turtle
ALIGNMENT = "Center"
FONT = ("Arial", 16, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.high_score = 0
        self.get_highscore()
        self.pendown()
        self.hideturtle()
        self.color("white")
        self.goto(10, 270)
        self.update_score()

    def update_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}        High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(10, 200)
        if self.score > self.high_score:
            with open("high_score.txt", mode="w") as f:
                f.write(str(self.score))
            self.write("New High Score!", align=ALIGNMENT, font=FONT)
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def get_highscore(self):
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
