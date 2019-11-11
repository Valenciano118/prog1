a=int(input("Introduce el lado a: "))
b=int(input("Introduce el lado b: "))
c=int(input("Introduce el lado c: "))

if a==b and c!=b or a==c and b!=c or b==c and a!=c:
    print("Es isósceles")
else:
    print("No es isósceles")