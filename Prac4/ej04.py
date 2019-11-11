def leer_lista_enteros():
    lista_leidos=[]
    print("Ve introduciendo números enteros, o una cadena vacía para acabar...")
    n=input("Nuevo número: ")
    while str(n)!="":
        lista_leidos.append(int(n))
        n = input("Nuevo número: ")
    return lista_leidos

lista_cuadrados=[]
lista_leidos=leer_lista_enteros()
for i in range(len(lista_leidos)):
    lista_cuadrados.append(lista_leidos[i]**2)

print("Cuadrados de los números leídos: {0}".format(lista_cuadrados))
print("Números leídos: {0}".format(lista_leidos))