from math import sin

lado1=float(input("Introduce el primer lado: "))
lado2=float(input("Introduce el segundo lado: "))
angulo=float(input("Introduce el ángulo (en radianes): "))

Área=(lado1*lado2/2)*sin(angulo)

print("El área del triángulo es: ",Área)