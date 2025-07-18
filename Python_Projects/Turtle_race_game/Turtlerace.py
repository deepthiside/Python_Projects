from turtle import Turtle,Screen
import random

is_race_on =False
screen = Screen()
screen.setup(width=500,height=500)
user_bet = screen.textinput(title="Make Your Bet",prompt= "Which turtle can win? enter a color")
color_choice= ["blue","green","black","yellow","red"]

y_position= [-90,-50,-20,20,60]
all_turtles = []
for turtle_index in range(5):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(color_choice[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()> 222:
            is_race_on= False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Yor Won! The winner is {winning_color} turtle ")
            else:
                print(f"you are lost, winner is {winning_color} turtle")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)



screen.exitonclick()