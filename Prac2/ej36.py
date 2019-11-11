n=int(input("Introduce un número entero: "))
fibonacci_actual=1
fibonacci_anterior=0
fibonacci_anterior2=0
for i in range(1,n):
    fibonacci_anterior=fibonacci_actual
    fibonacci_actual=fibonacci_anterior+fibonacci_anterior2
    fibonacci_anterior2 = fibonacci_anterior
print("Fibonacci({0}) = {1}".format(n,fibonacci_actual))
