consumo=int(input("Introduce la cantidad de kWh: "))

if consumo>0 and consumo<=100:
    importe=0.05*consumo
elif consumo>100 and consumo<=250:
    importe =(0.05*100)+0.07*(consumo-100)
else:
    importe=(0.05*100)+(0.07*150)+0.1*(consumo-250)

print("Importe: {:.2f} euros".format(importe))
