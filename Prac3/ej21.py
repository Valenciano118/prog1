def es_letra_castellana(x):
    letras_castellano="ñáéíóúü"
    letras_ingles="abcdefghijklmnopqrstuvwxyz"
    if not x.isdigit():
        x = x.lower()
    if x in letras_ingles or x in letras_castellano:
        return True
    else:
        return False
def primer_no_castellano(n):
    for i in range(len(n)):
        x=n[i]
        if not es_letra_castellana(x):
            return n[i]
print("Ve introduciendo palabras, o vacío para acabar...")
n=input("Nueva palabra: ")

while n!="":
    if primer_no_castellano(n)==None:
        print("Podría ser una palabra correcta ")
    else:
        print("Contiene un carácter que no es del alfabeto castellano: \'{0}\'".format(primer_no_castellano(n)))
    n=input("Nueva palabra: ")
print("¡Adiós!")