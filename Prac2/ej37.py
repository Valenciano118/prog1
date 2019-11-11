n=int(input("Introduce un número entero: "))
fibonacci_actual=1
fibonacci_anterior=0
fibonacci_anterior2=0
print("Los {0} primeros números de fibonacci son: ".format(n), end="")
for i in range(1,n+1):
    fibonacci_anterior=fibonacci_actual
    fibonacci_actual=fibonacci_anterior+fibonacci_anterior2
    fibonacci_anterior2 = fibonacci_anterior
    print(fibonacci_anterior,end=" ")