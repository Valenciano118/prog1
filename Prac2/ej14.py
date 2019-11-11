importe=float(input("Introduce el importe de la compra: "))
zona=input("Introduce la zona de envío (A/B/C): ")
socio=input("¿Eres socio (S/N)? ")

if importe>=0 and importe<=150:
    if socio=="S":
        importe_final=19
        if zona=="B":
            importe_final+=30
        if zona=="C":
            importe_final+=69
    else:
        importe_final=25
        if zona == "B":
            importe_final += 30
        if zona == "C":
            importe_final += 69

if importe>150 and importe<=750:
    if socio=="S":
        importe_final=49
        if zona=="B":
            importe_final+=30
        if zona=="C":
            importe_final+=69
    else:
        importe_final=60
        if zona == "B":
            importe_final += 30
        if zona == "C":
            importe_final += 69

if importe>750 and importe<=1500:
    if socio=="S":
        importe_final=89
        if zona=="B":
            importe_final+=30
        if zona=="C":
            importe_final+=69
    else:
        importe_final=120
        if zona == "B":
            importe_final += 30
        if zona == "C":
            importe_final += 69

if importe>1500 :
    if socio=="S":
        importe_final=importe*0.06
        if zona=="B":
            importe_final+=30
        if zona=="C":
            importe_final+=69
    else:
        importe_final=importe*0.08
        if zona == "B":
            importe_final += 30
        if zona == "C":
            importe_final += 69
print("Gastos de envío: {0:.2f} euros".format(importe_final))