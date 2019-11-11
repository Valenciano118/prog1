nombre_candidaturas=[]
votos_candidaturas=[]
votos_totales=0
print("Ve introduciendo candidaturas, o vacío para acabar...")
n=input("Nueva candidatura: ")
while n!="":
    nombre_candidaturas.append(n)
    n = input("Nueva candidatura: ")
for i in range(len(nombre_candidaturas)):
    n =int(input("Votos para {}: ".format(nombre_candidaturas[i])))
    votos_candidaturas.append(n)
    votos_totales+=n
for i in range(len(votos_candidaturas)):
    print("{0:.2f}% de los votos a candidaturas para {1}".format((votos_candidaturas[i]/votos_totales)*100,nombre_candidaturas[i]))