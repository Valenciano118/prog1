def contar_divisores(n):
    contador=0
    for i in range(1,n+1):
        if n%i==0:
            contador+=1
    return contador
def es_primo(n):
    if contar_divisores(n)==2:
        return True
    else:
        return False

a=int(input("Introduce un entero estrictamente positivo: "))
b=int(input("Introduce un entero mayor que {0}: ".format(a)))

print("Voy a buscar primos entre {0} y {1}...".format(a,b))

print("Encontrados: ",end="")
impresos=False
for i in range(a,b+1):
    if es_primo(i):
        print("{0}".format(i),end=" ")
        impresos=True
if impresos==False:
    print("ninguno",end=" ")