n=input("Introduce una cadena de caracteres: ")
contador=0
suma=0
for i in range(len(n)):
    x=n[i]
    if x.isdigit():
        contador+=1
        suma+=int(x)
    else:
        print("Primer \"no dígito\": \'{0}\' en posición {1}".format(x,i))
        break

if contador==len(n):
    print("Todos los caracteres son dígitos")
    print("¿Cuántos dígitos? {0}".format(len(n)))
    print("¿Suma de dígitos? {0}".format(suma))

