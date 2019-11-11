ángulo=int(input("Introduce un ángulo (en grados): "))

if ángulo==0:
    print("Nulo")
elif ángulo==360:
    print("Completo")
elif ángulo<90 and ángulo>0:
    print("Agudo")
elif ángulo==90:
    print("Recto")
elif ángulo<180 and ángulo>90:
    print("Obtuso")
elif ángulo==180:
    print("Llano")
elif ángulo<360 and ángulo>180:
    print("Cóncavo")
