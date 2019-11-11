def es_triángulo(a,b,c):
    if a+b>c and a+c>b and b+c>a:
     return True
    else:
        return False
a=float(input("Introduce el número a: "))
b=float(input("Introduce el número b: "))
c=float(input("Introduce el número c: "))

if es_triángulo(a,b,c)==True:
    print("Es un triángulo")
else:
    print("No es un triángulo")