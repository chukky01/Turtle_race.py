#import turtle and screen
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
#to set the width and the height of the screen that's going to show up
screen.setup(width=500, height=400)

#to be able to allow user input to be shown on screen
user_bet = screen.textinput(title="Make your bet", prompt="Which ninja-turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


#here we try to create 6 turtles for the game
for turtle_index in range(0, 6):
    # think of it like a graph, you have to specify the x and y cordinates for the turtles movements
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

#determining the movements of the six turtles
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            #check and print out the color of the winning ninja-turtle
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")



        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


#so that the screen does not go once it appears
screen.exitonclick()
