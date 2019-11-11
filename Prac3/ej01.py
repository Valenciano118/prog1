from math import pi
def área_círculo(r):
    área=pi*r**2
    return área
def longitud_circunferencia(r):
    longitud=2*pi*r
    return longitud
radio=float(input("Introduce el radio: "))
print("Área: {0:.2f}".format(área_círculo(radio)))
print("Longitud: {0:.2f}".format(longitud_circunferencia(radio)))

