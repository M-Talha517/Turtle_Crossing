from turtle import Turtle

#TO BE MADE GENERIC LATER ON
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.shapesize(0.7)
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        if self.xcor() >= STARTING_POSITION[0]:
            self.backward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)
