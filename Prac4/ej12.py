def leer_lista_enteros():
    lista_leidos=[]
    print("Ve introduciendo números enteros, o una cadena vacía para acabar...")
    n=input("Nuevo número: ")
    while str(n)!="":
        lista_leidos.append(int(n))
        n = input("Nuevo número: ")
    return lista_leidos
def repetidos_lista(lista):
    repetidos=[]
    for i in range(len(lista)):
        contador=0
        for n in range(i,len(lista)):
            if lista[i]==lista[n]:
                contador+=1
        if contador>1 and lista[i] not in repetidos:
            repetidos.append(lista[i])
    return repetidos
def suma_lista(lista):
    suma=0
    for i in range(len(lista)):
        suma+=lista[i]
    return suma
lista=leer_lista_enteros()

print("Números leídos más de una vez (suman {0}): {1}".format(suma_lista(repetidos_lista(lista)),repetidos_lista(lista)))
print("Todos los números leídos: {0}".format(lista))
