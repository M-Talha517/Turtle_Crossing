from turtle import Turtle

FONT = ("Courier", 24, "normal")


def save_highest_level(highest_level):
    with open(file='score.txt', mode='w') as score:
        score.write(highest_level)


def load_highest_level():
    try:
        with open(file='score.txt', mode='r') as score:
            highest_level = int(score.read())
    except FileNotFoundError:
        highest_level = 0
        save_highest_level(str(0))
    finally:
        return highest_level


class Scoreboard(Turtle):
    def __init__(self, starting_location):
        super(Scoreboard, self).__init__()
        self.level = 0
        self.penup()
        self.highest_level = load_highest_level()
        self.hideturtle()
        self.STARTING_POSITION = starting_location
        self.update()

    def update(self):
        self.clear()
        self.level += 1
        self.goto(self.STARTING_POSITION)
        self.write_text()

    def write_text(self):
        self.write(f"Level: {self.level}    Highest Level: {self.highest_level}", font=FONT)

    def gameover(self):
        if self.level > self.highest_level:
            self.highest_level = self.level
            save_highest_level(str(self.highest_level))

        self.goto(0, 0)
        self.write(f'GAME OVER', font=FONT, align="center", )
