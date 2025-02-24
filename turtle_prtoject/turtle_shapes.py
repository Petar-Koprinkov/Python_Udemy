from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.shape('turtle')
my_turtle.color('green')
my_colors = ['red', 'green', 'blue', 'yellow', 'purple', 'pink', 'brown', 'orange', 'black', 'grey', 'cyan']


def draw_shape(number_of_side):
    angel = 360 / number_of_side
    color = random.choice(my_colors)
    my_colors.remove(color)
    my_turtle.color(color)
    for _ in range(number_of_side):
        my_turtle.forward(100)
        my_turtle.left(angle=angel)


for sides_count in range(3, 11):
    draw_shape(sides_count)

screen = Screen()
screen.exitonclick()
