def difuminada(imagen,n):
    fila=len(imagen)
    col=len(imagen[0])
    imagen_nueva=nueva_matriz(fila,col,n)
    for i in range(1,fila-1):
        for j in range(1,col-1):
            imagen_nueva[i][j]=round(promedio_entorno(imagen,i,j))
    return imagen_nueva

def nueva_matriz(fila,col,inicial):
    matriz=[]
    for i in range(fila):
        matriz.append([inicial]*col)
    return matriz

def promedio_entorno(imagen,fila,col):
    promedio=0
    for i in range(fila-1,fila+2):
        for j in range(col-1,col+2):
            promedio+=imagen[i][j]
    promedio/=9
    return promedio

from moduloimagen import mostrarImagen,leerImagen

n=input("Introduce el nombre de la imagen: ")
borde=int(input("Introduce el valor del borde: "))

n=leerImagen(n)
mostrarImagen(difuminada(n,borde))