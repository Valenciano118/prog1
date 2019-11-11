num1=int(input("Introduce el primer número: "))
num2=int(input("Introduce el segundo número: "))
num3=int(input("Introduce el tercer número: "))

menor=num1

if num2<menor:
    menor=num2

if num3<menor:
    menor=num3

print("El menor es: ",menor)