import time
from turtle import Turtle, Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("white")
screen.title("Crossy Road")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")
screen.onkeypress(player.move_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.update_scoreboard()
    car_manager.create_cars()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()

    #detect crossing
    if player.ycor() > 280:
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()