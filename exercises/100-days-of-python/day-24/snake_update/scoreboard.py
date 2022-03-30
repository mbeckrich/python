from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("day-24/snake_update/data.txt", mode="r") as self.data:
            self.high_score_data = self.data.read()
        self.write(
            f"Score: {self.score}, High score: {self.high_score_data}",
            align=ALIGNMENT,
            font=FONT,
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("day-24/snake_update/data.txt", mode="w") as self.data:
                self.data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


# she uses int() to convert self.high_score = self.data.read()
