def producto_diagonal_secundaria(matriz):
    fila=len(matriz)
    producto=1
    if len(matriz)==len(matriz[0]):
        for i in range(fila):
            producto*=matriz[i][fila-i-1]
        return producto
from modulomatrices import leerMatrizEnteros
n=input("Introduce el nombre de un fichero: ")
matriz=leerMatrizEnteros(n)
if producto_diagonal_secundaria(matriz)==None:
    print("Error. Se requiere una matriz cuadrada")
else:
    print("El producto de los elementos en la  diagonal secundaria  es {0}".format(producto_diagonal_secundaria(matriz)))