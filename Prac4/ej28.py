def nueva_matriz(fila,col,inicial):
    matriz=[]
    for i in range(fila):
        matriz.append([inicial]*col)
    return matriz
def binarizada(matriz,umbral):
    matriz2=nueva_matriz(len(matriz),len(matriz[0]),umbral)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]>umbral:
                matriz2[i][j]=255
            else:
                matriz2[i][j]=0
    return matriz2
from moduloimagen import mostrarImagen,leerImagen
n=input("Introduce el nombre de la imagen: ")
umbral=int(input("Introduce el umbral: "))
n=leerImagen(n)

mostrarImagen(binarizada(n,umbral))
