plantilla=input("Introduce la plantilla de respuestas correctas: ")
print("Ve introduciendo respuestas de alumnos, o vacío para acabar...")
n=input("Nuevas respuestas: ")
alumnos = 0
while n!="":
    bien=0
    mal=0
    ns_nc=0
    if len(n)!=len(plantilla):
        print("La cadena introducida es de longitud {0} (se esperaba {1})".format(len(n),len(plantilla)))
    else:
        for i in range(len(n)):
            if n[i]==plantilla[i]:
                bien+=1
            elif n[i]=="*":
                ns_nc+=1
            else:
                mal+=1
        print("Resultados: {0} BIEN; {1} MAL; {2} NS/NC".format(bien,mal,ns_nc))
        alumnos+=1
    n=input("Nuevas respuestas: ")
print("Alumnos corregidos: {0}".format(alumnos))