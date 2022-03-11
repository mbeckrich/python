from turtle import Turtle

ALIGN = "center"
FONT = ("Mononoki Nerd Font Mono", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.write(
            f"Score: {self.score}",
            align=ALIGN,
            font=FONT,
        )

    # she uses function here called update_scoreboard() with the self.write
    # line, pervents using line twice.

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def calculate_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
