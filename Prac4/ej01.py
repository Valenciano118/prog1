lista_cadenas=[]
longitud_cadenas=[]
print("Ve introduciendo cadenas de caracteres, o vacío para acabar...")
n=input("Nueva cadena: ")
while n!="":
    lista_cadenas.append(n)
    longitud_cadenas.append(len(n))
    n = input("Nueva cadena: ")
print("Cadenas leídas: ")
for i in range(len(lista_cadenas)):
    print("Cadena de longitud {0}: =>{1}<=".format(longitud_cadenas[i],lista_cadenas[i]))
