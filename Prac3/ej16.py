n=input("Introduce una cadena de caracteres: ")
contador=0
for i in range(len(n)):
    x=n[i]
    if x.isdigit():
        contador+=1
if contador==len(n):
    print("Todos los caracteres son dígitos")
else:
    print("No todos los caracteres son dígitos")


