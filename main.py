import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.listen()

width = 600
height = 600
speed = 1

screen.setup(width=width, height=height)
screen.tracer(0)


player = Player()
car_manager = CarManager((width // 2, height // 2))
scoreboard = Scoreboard((-width // 2 + 20, height // 2 - 40))

screen.onkeypress(key='Up', fun=player.up)
screen.onkeypress(key='Down', fun=player.down)

def main():
    game_is_on = True
    while game_is_on:
        if not player.ycor() < height // 2 - 20:
            scoreboard.update()
            player.reset_position()
            car_manager.speedup()

        game_is_on = car_manager.forward(player)
        car_manager.create_car()
        time.sleep(0.1)
        screen.update()
    scoreboard.gameover()

main()

screen.exitonclick()
