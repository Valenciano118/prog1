def leer_lista_enteros():
    lista_leidos=[]
    print("Ve introduciendo números enteros, o una cadena vacía para acabar...")
    n=input("Nuevo número: ")
    while str(n)!="":
        lista_leidos.append(int(n))
        n = input("Nuevo número: ")
    return lista_leidos
def posición_menor(lista):
    minimo = lista[0]
    posicion = 0
    for i in range(len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
            posicion = i
    return posicion
def intercambiar(lista,j,i):
    if i!=j:
        aux = lista[i]
        lista[i] = lista[j]
        lista[j] = aux

lista=leer_lista_enteros()
if len(lista)==0:
    print("Lista leída: {0}".format(lista))
    print("Modificada: {0}".format(lista))
else:
    print("Lista leída: {0}".format(lista))
    intercambiar(lista,0,posición_menor(lista))
    print("Modificada: {0}".format(lista))