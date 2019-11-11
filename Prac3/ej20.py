letras_castellano="ñáéíóúü"
letras_ingles="abcdefghijklmnopqrstuvwxyz"
print("Ve introduciendo palabras, o vacío para acabar...")
n=input("Nueva palabra: ")

while n!="":
    contador=0
    for i in range(len(n)):
        x=n[i]
        if not x.isdigit():
            x=x.lower()
        if x in letras_ingles or x in letras_castellano:
            contador+=1
        else:
            print("Contiene un carácter que no es del alfabeto castellano: \'{0}\'".format(n[i]))
            break
    if contador==len(n):
        print("Podría ser una palabra correcta")
    n=input("Nueva palabra: ")
print("¡Adiós!")