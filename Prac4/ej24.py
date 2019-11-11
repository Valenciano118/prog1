def sumar_encima_diagonal(matriz):
    fila=len(matriz)
    suma=0
    if len(matriz)==len(matriz[0]):
        for i in range(0,fila-1):
            for j in range(i+1,fila):
              suma+=matriz[i][j]
        return suma
from modulomatrices import leerMatrizEnteros
n=input("Introduce el nombre de un fichero: ")
matriz=leerMatrizEnteros(n)
if sumar_encima_diagonal(matriz)==None:
    print("Error. Se requiere una matriz cuadrada")
else:
    print("La suma de los elementos por encima de la diagonal principal es {0}".format(sumar_encima_diagonal(matriz)))