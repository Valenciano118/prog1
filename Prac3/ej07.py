def contar_divisores(n):
    máximo_divisores=0
    n_maximo=0
    for x in range(1,n+1):
        contador_divisores=0
        for i in range (1,x+1):
            if x%i==0:
                contador_divisores+=1
        if contador_divisores>=máximo_divisores:
            n_maximo=x
            máximo_divisores=contador_divisores
    return n_maximo,máximo_divisores

n=int(input("Introduce un número entero: "))
x,y=contar_divisores(n)
print("El número con más divisores es {0} ({1} divisores)".format(x,y))