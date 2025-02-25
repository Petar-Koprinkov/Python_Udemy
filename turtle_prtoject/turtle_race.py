from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? (Enter the color):')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
y_coordinates = [-90, -50, -10, 30, 70, 110]

for index in range(0, 6):
    my_turtle = Turtle(shape='turtle')
    my_turtle.penup()
    my_turtle.color(colors[index])
    my_turtle.goto(x=-280, y=y_coordinates[index])

screen.exitonclick()
