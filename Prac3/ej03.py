def es_triángulo(a,b,c):
    if a+b>c and a+c>b and b+c>a:
         return True
    else:
        return False
def tipo_triángulo(a,b,c):
    if es_triángulo(a,b,c)==True:
        if a==b and b==c:
            return "equilátero"
        elif a==b and c!=a or a==c and b!=a or c==b and a!=c:
            return "isósceles"
        else:
            return "escaleno"
triángulo=False
while not triángulo:
    a=int(input("Introduce el lado a: "))
    b=int(input("Introduce el lado b: "))
    c=int(input("Introduce el lado c: "))
    if es_triángulo(a,b,c):
        print("Es {0}".format(tipo_triángulo(a,b,c)))
        triángulo=True
    else:print("No es un triángulo")


