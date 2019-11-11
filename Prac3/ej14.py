n=input("Introduce un texto (vacío para acabar): ")
longitud_maxima=len(n)
longitud_minima=100
cadena_maxima=""
cadena_minima=""

while n!="":
    if len(n)>=longitud_maxima:
        longitud_maxima=len(n)
        cadena_maxima=n
    if len(n)<=longitud_minima:
        longitud_minima=len(n)
        cadena_minima=n
    n=input("Introduce otro texto (vacío para acabar): ")
if longitud_maxima==0:
    print("No se ha introducido ningún texto")
else:
    print("Última cadena de mínima longitud, {0}: =>{1}<=".format(longitud_minima,cadena_minima))
    print("Última cadena de máxima longitud, {0}: =>{1}<=".format(longitud_maxima,cadena_maxima))