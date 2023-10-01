from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.traffic_list = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.creating_traffic()

    def creating_traffic(self):
        for i in range(random.randint(0, 4)):
            car = Turtle(shape="square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            car.setx(random.randint(290, 350))
            car.sety(random.randint(-230, 230))
            car.setheading(180)
            self.traffic_list.append(car)

    def traffic_move(self):
        for i in range(0, len(self.traffic_list)):
            self.traffic_list[i].forward(self.car_speed)

    def speed_increment(self):
        self.car_speed += MOVE_INCREMENT
