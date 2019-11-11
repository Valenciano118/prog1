def contar_secuencias_dígitos(cadena):
    secuencias=0
    anterior=' '
    for caracter in cadena:
        if caracter.isdigit() and not anterior.isdigit():
            secuencias+=1
        anterior=caracter
    return secuencias
print("Ve introduciendo cadenas de caracteres, o vacío para acabar...")
n=input("Nueva cadena: ")
while n!="":
    print("Secuencias de dígitos encontradas: {0}".format(contar_secuencias_dígitos(n)))
    n=input("Nueva cadena: ")
print("¡Adiós!")