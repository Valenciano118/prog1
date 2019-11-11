def leer_lista_enteros():
    lista_leidos=[]
    print("Ve introduciendo números enteros, o una cadena vacía para acabar...")
    n=input("Nuevo número: ")
    while str(n)!="":
        lista_leidos.append(int(n))
        n = input("Nuevo número: ")
    return lista_leidos
def ordenar_lista(lista):
    for i in range(len(lista)):
        intercambiar(lista,i,posición_menor(lista,i))

def posición_menor(lista,n):
    minimo = lista[n]
    posicion = n
    for i in range(n,len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
            posicion = i
    return posicion

def intercambiar(lista, j, i):
        aux = lista[i]
        lista[i] = lista[j]
        lista[j] = aux

lista=leer_lista_enteros()
if len(lista)==0 or len(lista)==1:
    print("Lista leída: {0}".format(lista))
    print("Lista ordenada: {0}".format(lista))
else:
    print("Lista leída: {0}".format(lista))
    ordenar_lista(lista)
    print("Lista ordenada: {0}".format(lista))