from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.shape('turtle')
my_turtle.color('green')
my_colors = ['red', 'green', 'blue', 'yellow', 'purple', 'pink', 'brown', 'orange', 'black', 'grey', 'cyan']
angels = [0, 90, 180, 270]


def walk():
    my_turtle.setheading(random.choice(angels))
    my_turtle.width(9)
    my_turtle.speed(20)
    my_turtle.forward(20)


for _ in range(250):
    my_turtle.color(random.choice(my_colors))
    walk()

screen = Screen()
screen.exitonclick()
