n=int(input("Introduce un número entero: "))
divisores=1
for i in range(1,n//2+1):
    if n%i==0:
        divisores+=1
print("El número {0} tiene {1} divisores".format(n,divisores))
