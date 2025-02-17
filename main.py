import time
from turtle import Turtle, Screen
from player import Player

screen = Screen()
screen.bgcolor("white")
screen.title("Crossy Road")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkeypress(player.move, "Up")
screen.onkeypress(player.move_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()