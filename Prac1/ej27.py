import turtle

pantalla=turtle.Screen()
pantalla.setup(425,425)
pantalla.screensize(400,400)
pantalla.setworldcoordinates(-400,-400,400,400)

tortuga=turtle.Turtle()

x=int(input("Introduce las coordenadas x: "))
y=int(input("Introduce las coordenadas y: "))
r=int(input("Introduce el radio; "))


tortuga.penup()
tortuga.goto(x,y)
tortuga.pendown()
tortuga.circle(r)
tortuga.penup()
tortuga.goto(x,y+r*3/2)
tortuga.pendown()
tortuga.circle(r/2)
pantalla.exitonclick()