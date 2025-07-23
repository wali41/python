import turtle

sc= turtle.Screen()
sc.bgcolor("yellow")
sc.setup(400,300)


triangle =turtle.Turtle()

triangle.color("purple")
triangle.pensize(10)

triangle.forward(100)
triangle.left(120)

triangle.forward(100)
triangle.left(120)

triangle.forward(100)

sc.exitonclick()