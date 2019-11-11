n=int(input("Introduce un número entero: "))
producto_total=1
tiene_factorial=False
i=1
while i<=n and not tiene_factorial:
    producto_total*=i
    if producto_total==n:
        tiene_factorial=True
        print("{0} es el factorial de {1}".format(n,i))
    if i==n and tiene_factorial==False:
        print("{0} no tiene factorial".format(n))
    i+=1