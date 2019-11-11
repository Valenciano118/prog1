def leer_lista_enteros():
    lista_leidos=[]
    print("Ve introduciendo números enteros, o una cadena vacía para acabar...")
    n=input("Nuevo número: ")
    while str(n)!="":
        lista_leidos.append(int(n))
        n = input("Nuevo número: ")
    return lista_leidos

lista_leidos=leer_lista_enteros()
print("Lista leída: {0}".format(lista_leidos))
n=input("¿Qué suma he de buscar en dos posiciones consecutivas? ")
while n!="":
    for i in range(len(lista_leidos))