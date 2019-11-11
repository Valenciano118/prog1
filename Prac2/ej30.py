n=float(input("Introduce un número: "))
suma=0
minimo=10
maximo=0
contador=0
while n>0:
    contador+=1
    suma+=n
    if n>maximo:
        maximo=n
    if n<minimo:
        minimo=n
    n=float(input("Introduce otro número: "))
if suma==0:
    print("No se han introducido datos ")
else:
    print("Media: {0}".format(suma/contador))
    print("Mínimo: {0}".format(minimo))
    print("Máximo: {0}".format(maximo))