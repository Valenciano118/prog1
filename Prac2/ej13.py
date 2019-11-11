visitas=int(input("¿Cuántas veces prevés utilizar el gimnasio? "))

coste_tarjeta=50
coste_bono=20
coste_entrada=3
mejor_precio=coste_tarjeta
mejor_oferta="tarjeta."
usos_bono=10
usos_entrada=1

if visitas%usos_bono !=0:
    bono=visitas//usos_bono +1
else:
    bono=visitas//usos_bono

if visitas%usos_bono !=0:
    bono2=visitas//usos_bono
    entrada=visitas-(usos_bono*bono2)
else:
    bono2=visitas//usos_bono
    entrada=0
if coste_bono*bono<mejor_precio:
    mejor_precio=coste_bono*bono
    mejor_oferta="bonos."
if (coste_bono*bono2+coste_entrada*entrada)<mejor_precio:
    mejor_precio=coste_bono*bono2+coste_entrada*entrada
    mejor_oferta="bonos y entradas."



print("Con tarjeta: 50 euros.")
print("Con bonos ({0}): {1} euros.".format(bono,coste_bono*bono))
print("Con bonos ({0}) y entradas ({1}): {2} euros.".format(bono2,entrada,coste_bono*bono2+coste_entrada*entrada))
print("Recomendación: {0} ".format(mejor_oferta))
