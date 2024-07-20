import turtle

dist = 1
flag = 500

spiral = turtle.Turtle()

spiral.speed(10)

while flag:
    spiral.forward(dist)

    spiral.left(120)
    spiral.left(1)
    dist += 1
    flag -= 1

turtle.done()