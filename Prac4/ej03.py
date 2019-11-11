lista_pares=[]
lista_impares=[]
print("Ve introduciendo números enteros positivos, o un número negativo para acabar...")
n=int(input("Nuevo número: "))
while n>=0:
    if n%2==0:
        lista_pares.append(n)
    else:
        lista_impares.append(n)
    n = int(input("Nuevo número: "))
print("Números pares: {0}".format(lista_pares))
print("Números impares: {0}".format(lista_impares))