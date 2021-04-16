from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, starting_location):
        super(Scoreboard, self).__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.STARTING_POSITION = starting_location
        self.update()

    def update(self):
        self.clear()
        self.level += 1
        self.goto(self.STARTING_POSITION)
        self.write_text()

    def write_text(self):
        self.write(f"Level: {self.level}", font=FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', font=FONT, align="center",)