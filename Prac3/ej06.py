def contar_divisores(n):
    contador=0
    for i in range(1,n+1):
        if n%i==0:
            contador+=1
    return contador

n=int(input("Introduce un número entero: "))
print("El número {0} tiene {1} divisores".format(n,contar_divisores(n)))