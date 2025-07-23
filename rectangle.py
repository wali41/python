import turtle

sc = turtle.Screen()
sc.bgcolor("yellow")
sc.setup(500,500)

rectangle =turtle.Turtle()

rectangle.color("blue")
rectangle.pensize(6)

for i in range (2):

    rectangle.forward(200)
    rectangle.left(90)

    rectangle.forward(100)
    rectangle.left(90)


sc.exitonclick()






























