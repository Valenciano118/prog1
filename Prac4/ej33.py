def nueva_matriz(fila,col,inicial):
    matriz=[]
    for i in range(fila):
        matriz.append([inicial]*col)
    return matriz
def girada_izquierda(imagen):
    fila=len(imagen)
    col=len(imagen[0])
    imagen_nueva=nueva_matriz(col,fila,0)
    fila_nueva=col
    col_nueva=fila
    for i in range(fila_nueva):
        for j in range(col_nueva):
            imagen_nueva[i][j]=imagen[j][col-i-1]
    return imagen_nueva

from moduloimagen import mostrarImagen,leerImagen
n=input("Introduce el nombre de la imagen: ")
n=leerImagen(n)
mostrarImagen(girada_izquierda(n))