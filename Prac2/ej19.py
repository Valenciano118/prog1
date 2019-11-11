triángulo=False
while not triángulo:
    a = int(input("Introduce el lado a: "))
    b = int(input("Introduce el lado b: "))
    c = int(input("Introduce el lado c: "))
    if a+b>c and a+c>b and b+c>a:
        triángulo=True
        if a==b and b==c:
            print("Es equilátero")
        elif a==b and c!=a or a==c and b!=a or c==b and a!=c:
            print("Es isósceles")
        else:
            print("Es escaleno")
    else:
        print("No es un triángulo")
