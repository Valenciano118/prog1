n=int(input("Introduce un número entero: "))

for i in range(1,n):
    cuadrado=i**2
    if cuadrado<n:
        print("El cuadrado de {0} es {1}".format(i,cuadrado))
