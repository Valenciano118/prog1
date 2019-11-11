n=int(input("Introduce un número entero: "))
contador=0
candidato=1
def es_primo(n):
    divisores=0
    for i in range(1,n+1):
        if n%i==0:
            divisores+=1
    if divisores==2:
        return n
print("Los {0} primeros números primos son: ".format(n),end="")
while contador<n:
    if es_primo(candidato)==candidato:
        contador+=1
        print(candidato,end=" ")
    candidato+=1
