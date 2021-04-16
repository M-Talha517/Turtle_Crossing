from random import choice, randint, randrange
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


def detect_collision(car, player):
    # 10 units from centre to Turtle + 20 units from centre of car (horizontally)
    if -30 < car.xcor() - player.xcor() < 30:
        # 10 units from centre to Turtle + 10 units from centre of car (vertically)
        if -20 < car.ycor() - player.ycor() < 20:
            return True


class CarManager:
    def __init__(self, starting_position):
        self.car_list = []
        self.STARTING_X_CORD = starting_position[0]
        self.Y_LIMIT = starting_position[1] - 50
        self.speed = STARTING_MOVE_DISTANCE
        self.game_board(Turtle(), starting_position)

    def game_board(self, creator, starting_position):
        headings = [0, 180]
        count = 1
        creator.penup()
        creator.setheading(180)
        creator.goto(self.STARTING_X_CORD, -starting_position[1]+35)
        for i in range(0, starting_position[1]*2 - 80, 30):
            for j in range(0, starting_position[0]*2, 40):
                creator.pendown()
                creator.forward(5)
                creator.penup()
                creator.forward(35)
            count += 1
            creator.setheading(90)
            creator.forward(30)
            creator.setheading(headings[count % 2])

    def speedup(self):
        self.speed += MOVE_INCREMENT

    def create_car(self):
        if randint(1, 6) == 6:
            car = Turtle('square')
            car.penup()
            car.setheading(180)
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(choice(COLORS))
            car.goto(self.STARTING_X_CORD, randrange(-self.Y_LIMIT, self.Y_LIMIT, 30))
            self.car_list.append(car)

    def forward(self, player):
        for car in self.car_list:
            car.forward(self.speed)
            if detect_collision(car, player):
                return False
            if car.xcor() < -self.STARTING_X_CORD - 20:
                car.hideturtle()
                self.car_list.remove(car)
        return True
