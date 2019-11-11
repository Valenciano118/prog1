def mostrar_cadena_repetida(c,n,s):
    print((c+s)*(n-1)+c)
c=input("Introduce una cadena: ")
s=input("Introduce un separador: ")
m=int(input("Introduce un máximo de repeticiones: "))

for n in range(1,m+1):
    mostrar_cadena_repetida(c,n,s)
