#spiralhelixcolorful

import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("Python Turtle")

turtle_instance = turtle.Turtle()
turtle_instance.color("white")
turtle.speed(0)
colorslist=["red", "blue", "orange","green", "purple", "yellow"]

for i in range(20):
    turtle_instance.color(colorslist[i%6])
    turtle_instance.circle(10*i)
    turtle_instance.circle(-10*i)
    turtle_instance.left(i)

turtle.mainloop()
turtle.done()