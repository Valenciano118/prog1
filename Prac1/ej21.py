from math import pi

def área_circulo(radio):
    return pi*radio**2

radio=float(input("Introduce el radio: "))

print("Área:",área_circulo(radio))