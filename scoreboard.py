from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.scores = 0
        # self.high_score = int(contents)
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(0, 275)
        self.write(arg=f"Score: {self.scores}", move=False, align=ALIGNMENT, font=FONT)

    def add_scores(self):
        self.scores += 1
        self.clear()
        self.write(arg=f"Score: {self.scores}  High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="Game over.", move=False, align=ALIGNMENT, font=FONT)

    # how to set and track high scores
    def reset(self):
        if self.scores > self.high_score:
            self.high_score = self.scores
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.scores = 0
        self.clear()
        self.write(arg=f"Score: {self.scores}  High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
