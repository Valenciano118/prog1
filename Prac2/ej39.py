n=int(input("Introduce un número entero: "))
candidato_primo=1
print("Los números primos menores que {0} son: ".format(n),end="")
while candidato_primo<n:
    divisores=0
    for i in range(1,n+1):
        if candidato_primo%i==0:
            divisores+=1
    if divisores==2:
        print(candidato_primo,end=" ")
    candidato_primo+=1