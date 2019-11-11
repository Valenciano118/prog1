def leer_lista_enteros():
    lista_leidos=[]
    print("Ve introduciendo números enteros, o una cadena vacía para acabar...")
    n=input("Nuevo número: ")
    while str(n)!="":
        lista_leidos.append(int(n))
        n = input("Nuevo número: ")
    return lista_leidos
def borrar_elemento(lista,n):
    if n>=0 and n<len(lista):
        del lista[n]
        return True
    return False

lista_leidos=leer_lista_enteros()

while len(lista_leidos)>0:
    n=int(input("¿Qué posición debo eliminar de {0}? ".format(lista_leidos)))
    if borrar_elemento(lista_leidos,n):
        borrar_elemento(lista_leidos,n)
    else:
        print("Posición Incorrecta")
print("La lista ha quedado vacía")