import turtle

pantalla=turtle.Screen()
pantalla.setup(425,425)
pantalla.screensize(400,400)
pantalla.setworldcoordinates(-400,-400,400,400)

tortuga=turtle.Turtle()

coordenadas=int(input("Introduce un número entero (Este define el radio y las coordenadas de la circunferencia"))
tortuga.penup()
tortuga.setx(coordenadas)
tortuga.sety(coordenadas)
tortuga.pendown()
tortuga.circle(coordenadas)

pantalla.exitonclick()
