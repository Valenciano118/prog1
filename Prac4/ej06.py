def leer_lista_enteros():
    lista_leidos=[]
    print("Ve introduciendo números enteros, o una cadena vacía para acabar...")
    n=input("Nuevo número: ")
    while str(n)!="":
        lista_leidos.append(int(n))
        n = input("Nuevo número: ")
    return lista_leidos
def borrar_elemento(lista,n):
    for i in range(len(lista)):
        if lista[i]==n:
            del lista[i]
            return True
    return False

lista_leidos=leer_lista_enteros()
while len(lista_leidos)>0:
    n=int(input("¿Qué número debo eliminar de {0}? ".format(lista_leidos)))
    if borrar_elemento(lista_leidos,n)==False:
        print("Número no encontrado")
print("La lista ha quedado vacía")
