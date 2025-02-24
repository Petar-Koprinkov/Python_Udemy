import turtle
from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.shape('turtle')
my_turtle.color('green')
angels = [0, 90, 180, 270]
turtle.colormode(255)


def random_color():
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    color = (r, g, b)
    return color


def walk():
    my_turtle.setheading(random.choice(angels))
    my_turtle.width(9)
    my_turtle.speed(20)
    my_turtle.forward(20)


for _ in range(250):
    my_turtle.color(random_color())
    walk()

screen = Screen()
screen.exitonclick()
