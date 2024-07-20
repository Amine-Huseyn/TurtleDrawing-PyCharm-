#shrinking square
import turtle

turtle_screen=turtle.Screen()
turtle_screen.bgcolor("white")
turtle_screen.title=("turtle python")

turtleins=turtle.Turtle()
turtleins.color= ("red")

def shrinkingsquare(size):
    for i in range(4):
        turtleins.forward(size)
        turtleins.left(90)
        size = size-5

shrinkingsquare(400)
shrinkingsquare(380)
shrinkingsquare(360)
shrinkingsquare(340)
shrinkingsquare(320)
shrinkingsquare(300)
shrinkingsquare(280)
shrinkingsquare(260)
shrinkingsquare(240)
shrinkingsquare(220)
shrinkingsquare(200)
shrinkingsquare(180)
shrinkingsquare(160)
shrinkingsquare(140)
shrinkingsquare(120)
shrinkingsquare(100)

turtle.done()
