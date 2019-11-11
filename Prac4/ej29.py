def reflejar_horizontal(matriz):
    fila=len(matriz)
    col=len(matriz[0])
    for i in range(fila):
        for j in range(col // 2):
            aux = matriz[i][j]
            matriz[i][j] = matriz[i][col - j - 1]
            matriz[i][col - j - 1] = aux
    mostrarImagen(matriz)
from modulomatrices import leerMatrizEnteros
from moduloimagen import mostrarImagen

n=input("Introduce el nombre de la imagen:")
n=leerMatrizEnteros(n)
reflejar_horizontal(n)