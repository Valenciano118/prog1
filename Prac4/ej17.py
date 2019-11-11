def evaluación_test(plantilla,respuestas):
    resultado=[0,0,0]
    if len(plantilla)==len(respuestas):
        for i in range(len(plantilla)):
            if respuestas[i]=="*":
                resultado[2]+=1
            elif respuestas[i]==plantilla[i]:
                resultado[0]+=1
            else:
                resultado[1]+=1
        return resultado

plantilla=input("Introduce la plantilla de respuestas correctas: ")
contador=0
print("Ve introduciendo respuestas de alumnos, o vacío para acabar... ")
respuesta=input("Nuevas respuestas: ")
while respuesta!="":
    if evaluación_test(plantilla,respuesta)==None:
        print("La cadena introducida es de longitud {0} (se esperaba {1})".format(len(respuesta),len(plantilla)))
    else:
        resultados=evaluación_test(plantilla,respuesta)
        print("Resultados: {0} BIEN; {1} MAL; {2} NS/NC".format(resultados[0],resultados[1],resultados[2]))
        contador+=1
    respuesta = input("Nuevas respuestas: ")
print("alumnos corregidos: {0}".format(contador ))


