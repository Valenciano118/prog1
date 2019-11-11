n=int(input("Introduce un número entero: "))
fibonacci_actual=1
fibonacci_anterior=0
fibonacci_anterior2=0
printed=False
for i in range(1,n+1):
    fibonacci_anterior=fibonacci_actual
    fibonacci_actual=fibonacci_anterior+fibonacci_anterior2
    fibonacci_anterior2 = fibonacci_anterior
    if fibonacci_actual == n:
        print("El número buscado es {0}".format(i+1))
        printed = True

if not printed:
    print("No es un número de Fibonacci")