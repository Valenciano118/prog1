import turtle
from math import sqrt

pantalla=turtle.Screen()
pantalla.setup(425,425)
pantalla.screensize(400,400)
pantalla.setworldcoordinates(-400,-400,400,400)

tortuga=turtle.Turtle()
x=0
lado=int(input("Introduce el lado del cuadrado: "))

tortuga.penup()
tortuga.goto(-lado/2,-lado/2)
tortuga.setheading(0)
tortuga.pendown()
while x !=4:

    x=x+1
    tortuga.forward(lado)
    tortuga.left(90)
tortuga.setheading(45)
tortuga.forward(lado*sqrt(2))
tortuga.penup()
tortuga.goto(-lado/2,lado/2)
tortuga.pendown()
tortuga.right(90)
tortuga.forward(lado*sqrt(2))
pantalla.exitonclick()