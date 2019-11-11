from math import sqrt

a=float(input("Introduce a: "))
b=float(input("Introduce b: "))
c=float(input("Introduce c: "))

x1=(-b+sqrt(b**2-4*a*c))/(2*a)
x2=(-b-sqrt(b**2-4*a*c))/(2*a)

print("x1 = ",x1)
print("x2 = ",x2)