def sumar_divisores_propios(n):
    suma=0
    for i in range(1,n):
        if n%i==0:
            suma+=i
    return suma
def es_abundante(n):
    if n<sumar_divisores_propios(n):
        return True
    else:
        return False

n=int(input("Introduce un número entero: "))
print("Los números abundantes menores que {0} son: ".format(n),end="")
for i in range(1,n):
    if es_abundante(i) and i<n:
        print("{0}".format(i),end=" ")
