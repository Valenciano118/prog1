num1=int(input("Introduce el primer número: "))
num2=int(input("Introduce el segundo número: "))
num3=int(input("Introduce el tercer número: "))
num4=int(input("Introduce el cuarto número: "))

menor=num1

if num2<menor:
    menor=num2

if num3<menor:
    menor=num3

if num4<menor:
    menor=num4

print("El menor es: ",menor)