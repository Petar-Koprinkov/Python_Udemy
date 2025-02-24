from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.shape('turtle')
my_turtle.color('green')

sides = 3
repeats = 1
my_color = ['red', 'green', 'blue', 'yellow', 'purple', 'pink', 'brown', 'orange', 'black']

while repeats < 7:
    color = random.choice(my_color)
    my_color.remove(color)
    for _ in range(sides):
        angel = 360 / sides
        my_turtle.color(color)
        my_turtle.forward(100)
        my_turtle.left(angle=angel)

    sides += 1
    repeats += 1


screen = Screen()
screen.exitonclick()