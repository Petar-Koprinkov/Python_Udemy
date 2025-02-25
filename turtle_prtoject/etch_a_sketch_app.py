from turtle import Turtle, Screen

my_turtle = Turtle()


def move_forward():
    my_turtle.forward(10)


def move_backward():
    my_turtle.backward(10)


def turn_left():
    my_turtle.left(10)


def turn_right():
    my_turtle.right(10)


screen = Screen()
screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='space', fun=my_turtle.reset)
screen.exitonclick()
