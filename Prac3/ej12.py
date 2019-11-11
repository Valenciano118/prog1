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
def leer_entero_mayor_que(n):
    enteros=[]
    while len(enteros)<2:
        b = int(input("Introduce un número entero mayor que {0}: ".format(n)))
        while b<=n:
            b=int(input("Esperaba entero mayor que {0} y {1} no lo es. Dame otro: ".format(n,b)))
        n=b
        enteros.append(b)
    return enteros

enteros=leer_entero_mayor_que(0)
print("Voy a buscar primos entre {0} y {1}...".format(enteros[0],enteros[1]))

print("Encontrados: ",end="")
for i in range(enteros[0],enteros[1]+1):
    if es_primo(i):
        print(i,end=" ")