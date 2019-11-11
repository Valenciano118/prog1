n=int(input("Introduce un número entero: "))
factorial=1
for i in range(1,n+1):
    factorial*=i
print("{0}! = {1}".format(n,factorial))