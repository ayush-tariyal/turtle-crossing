from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing")
screen.tracer(0)

player = Player()
traffic = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.move, key="space")

game_loop = 0

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    game_loop += 1
    if game_loop % 6 == 0:
        traffic.creating_traffic()

    # Move the cars forward
    traffic.traffic_move()

    # Detect collision with the car
    for car in traffic.traffic_list:
        if car.distance(player) < 12:
            is_game_on = False
            score.game_over()

    # If the player successfully crossed the road
    if player.ycor() >= 300:
        player.player_reset()
        traffic.speed_increment()
        score.new_score()


screen.exitonclick()
