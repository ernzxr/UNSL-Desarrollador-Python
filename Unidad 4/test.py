# //////// Ejercicio 12 ////////
print("\nEjercicio 12")

def factorial(n):
    if n < 0:
        raise print("No se puede calcular el factorial en numeros negativos.")
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        raise print("No se aplican los numeros negativos a la serie de Fibonacci.")
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def potencia(n, m):
        return n ** m

try:
    n = int(input("Ingrese un número entero para calcular el factorial: "))
    print(f"El factorial de {n} es {factorial(n)}")
except:
    print("El valor ingresado no es valido.")

try:
    n = int(input("Ingrese un número entero para calcular el término de Fibonacci: "))
    print(f"El término {n} de la serie de Fibonacci es {fibonacci(n)}")
except:
    print("El valor ingresado no es valido.")

try:
    n = float(input("Ingrese la base de la potencia (n): "))
    m = int(input("Ingrese el exponente de la potencia (m): "))
    print(f"{n} elevado a la potencia {m} es igual a {potencia(n, m)}")
except:
    print("El valor ingresado no es valido.")