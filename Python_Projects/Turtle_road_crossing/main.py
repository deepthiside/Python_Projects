import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


tinku = Player((0,-280))
screen.listen()
screen.onkey(tinku.go_up, "Up")

car_manager = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # if tinku.ycor()> 300 or tinku.ycor()<-300:
    #     tinku.Win()

    for car in car_manager.all_cars:
        if car.distance(tinku)<20:
            game_is_on = False

    if tinku.is_at_finish_line():
        tinku.go_to_start()
        car_manager.level_up()
        score.increase_level()

screen.exitonclick()
