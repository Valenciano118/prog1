def reflejar_vertical(imagen):
    fila=len(imagen)
    col=len(imagen[0])
    for i in range(fila//2):
        for j in range(col):
            aux=imagen[i][j]
            imagen[i][j]=imagen[fila-1-i][j]
            imagen[fila - 1 - i][j]=aux
    mostrarImagen(imagen)


from moduloimagen import mostrarImagen,leerImagen

n=input("Introduce el nombre de la imagen: ")
n=leerImagen(n)
reflejar_vertical(n)
