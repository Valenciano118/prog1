import turtle

pantalla=turtle.Screen()
pantalla.setup(425,425)
pantalla.screensize(400,400)
pantalla.setworldcoordinates(-400,-400,400,400)

tortuga=turtle.Turtle()

x=int(input("Introduce las coordenadas: "))
r=int(input("Introduce el radio; "))

tortuga.penup()
tortuga.goto(x,x)
tortuga.pendown()
tortuga.circle(r)
tortuga.penup()
tortuga.goto(x,x+r)
tortuga.setheading(45)
tortuga.pendown()
tortuga.forward(r)

pantalla.exitonclick()