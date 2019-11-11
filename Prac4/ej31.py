def promedio_entorno(imagen,fila,col):
    promedio=0
    for i in range(fila-1,fila+2):
        for j in range(col-1,col+2):
            promedio+=imagen[i][j]
    promedio/=9
    return promedio
from moduloimagen import leerImagen

n=input("Introduce el nombre de la imagen: ")
n=leerImagen(n)

fila=int(input("Introduce un número de fila: "))
col=int(input("Introduce un número de columna: "))
n=promedio_entorno(n,fila,col)

print("El promedio en el entorno del punto ({0},{1}) es {2:.2f}".format(fila,col,n))
