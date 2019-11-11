import turtle
from math import sqrt
pantalla=turtle.Screen()
pantalla.setup(425,425)
pantalla.screensize(400,400)
pantalla.setworldcoordinates(-400,-400,400,400)

tortuga=turtle.Turtle()
lado=int(input("Introduce el lado del triangulo equilatero: "))

tortuga.penup()
tortuga.goto(0,lado*sqrt(3)/2)
tortuga.pendown()
tortuga.goto(-lado/2,0)
tortuga.goto(lado/2,0)
tortuga.goto(0,lado*sqrt(3)/2)
pantalla.exitonclick()





