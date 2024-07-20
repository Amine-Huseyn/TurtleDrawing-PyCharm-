import turtle
drawing_board = turtle.Screen()
drawing_board.bgcolor("white")
drawing_board.title("Python Turtle")

#spolygon
turtle_instance = turtle.Turtle()
numside=6
angle=360/numside
sidelenght = 100
for i in range(6):
    turtle_instance.forward(sidelenght)
    turtle_instance.right(angle)


turtle.done()