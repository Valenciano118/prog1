def leer_alturas():
    lista_alturas=[]
    punto_kilometrico=0
    print("Ve introduciendo alturas sobre el nivel del mar, o una cadena vacía para acabar...")
    n=input("Altura en metros en el punto kilométrico {0}:".format(punto_kilometrico))
    while n!="":
        lista_alturas.append(int(n))
        punto_kilometrico+=1
        n = input(" Altura en metros en el punto kilométrico {0}: ".format(punto_kilometrico))
    return lista_alturas
def calcular_desniveles(lista_alturas):
    lista_desniveles=[]
    for i in range(len(lista_alturas)-1):
        lista_desniveles.append(lista_alturas[i+1]-lista_alturas[i])
    return lista_desniveles
def posición_máximo(lista):
    máximo=-1
    posición=0
    for i in range(len(lista)):
        if lista[i]>=máximo:
            máximo=lista[i]
            posición=i

    return posición
lista_alturas=leer_alturas()
if len(lista_alturas)<=1:
    print(" Recorrido no válido, con menos de dos puntos")
else:

    lista_desniveles=calcular_desniveles(lista_alturas)
    desnivel=False

    print("Lista de alturas: {0}".format(lista_alturas))
    print("Lista de desniveles: {0}".format(lista_desniveles))
    for i in range(len(lista_desniveles)):
        if lista_desniveles[i]>0:
            desnivel=True
            break
    if desnivel:
        print("Kilómetro con mayor desnivel de subida: \n \t Entre los puntos kilométricos {0} y {1} \n \t Desnivel de {2} m".format(posición_máximo(lista_desniveles), posición_máximo(lista_desniveles) + 1,abs(lista_desniveles[posición_máximo(lista_desniveles)])))
    else:
        print("Ningún kilómetro es de subida")

