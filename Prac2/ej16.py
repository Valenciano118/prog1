n=int(input("Introduce un número entero: "))
print("",end="")
for i in range (1,n+1):
    if n==1 or i==n:
        print(i,end="")
    else:
        print(i,end=", ")