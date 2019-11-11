a=input("Introduce una cadena de caracteres A: ")
b=input("Introduce una cadena de caracteres B: ")
if a[len(a)-len(b):]==b:
    print("B es sufijo de A")
elif b=="":
    print("B es sufijo de A")
else:
    print("B no es sufijo de A")