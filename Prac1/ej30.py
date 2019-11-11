import turtle

pantalla=turtle.Screen()
pantalla.setup(425,425)
pantalla.screensize(400,400)
pantalla.setworldcoordinates(-400,-400,400,400)

tortuga=turtle.Turtle()
lado1=int(input("Introduce el lado del cateto1: "))
lado2=int(input("Introduce el lado del cateto2: "))


if lado1>=lado2:
    cateto1=lado1
    cateto2=lado2
else:
    cateto1=lado2
    cateto2=lado1

tortuga.penup()
tortuga.goto(0,0)
tortuga.setheading(0)
tortuga.pendown()
tortuga.forward(cateto1)
tortuga.penup()
tortuga.goto(0,0)
tortuga.setheading(90)
tortuga.pendown()
tortuga.forward(cateto2)
tortuga.goto(cateto1,0)
pantalla.exitonclick()
