from math import pi
from math import sin
a=float(input("Introduce el primer lado: "))
b=float(input("Introduce el segundo lado: "))
Ángulo=float(input("Introduce el ángulo (en grados): "))

Área=a*b*(sin(Ángulo*pi/180))/2

print("El área del triángulo es: {:.14f}".format(Área))