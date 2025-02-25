from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? (Enter the color):').lower()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
y_coordinates = [-90, -50, -10, 30, 70, 110]
all_turtles = []
still_racing = False

for index in range(0, 6):
    my_turtle = Turtle(shape='turtle')
    my_turtle.penup()
    my_turtle.color(colors[index])
    my_turtle.goto(x=-280, y=y_coordinates[index])
    all_turtles.append(my_turtle)

if user_bet in colors:
    still_racing = True


while still_racing:
    for turtle in all_turtles:
        if turtle.xcor() >= 270:
            still_racing = False
            if turtle.pencolor() == user_bet:
                print(f'You have won! The winner of the race is {turtle.pencolor()} turtle')
            else:
                print(f'You have lost! The winner of the race is {turtle.pencolor()} turtle')
        turtle.forward(random.randint(0, 10))


screen.exitonclick()
