n=int(input("Introduce un número entero: "))
tiene_factorial=False
i=1
while i<n and not tiene_factorial:
    producto_total=1
    for x in range(1,i+1):
        producto_total*=x
    if producto_total>n:
        tiene_factorial=True
        print("El número buscado es {0} ({1}! <= {2} < {3}!)".format(i,i-1,n,i))
    i+=1