# noinspection LossyEncoding
# //////// Ejercicio 1 ////////
print("\nEjercicio 1")

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

print(f"Factorial de 4: {factorial(4)}")

# //////// Ejercicio 2 ////////
print("\nEjercicio 2")

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Fibonacci de 5: {fibonacci(5)}")

# //////// Ejercicio 3 ////////
print("\nEjercicio 3")

def euclides(a, b):
    if b == 0:
        return a
    else:
        return euclides(b, a % b)

print(f"mcd de 30 y 24: {euclides(30, 24)}")

# //////// Ejercicio 4 ////////
print("\nEjercicio 4")

def recursivaT(n):
    if n == 0 or n == 1:
        return 3
    elif n > 1:
        return 7 + recursivaT(n / 2)

print(f"recursivaT de 8: {recursivaT(8)}")

# //////// Ejercicio 5 ////////
print("\nEjercicio 5")

def triangular(n):
    return 1 if n == 1 else n + triangular(n - 1)

print(f"Triangular de 10: {triangular(10)}")

# //////// Ejercicio 6 ////////
print("\nEjercicio 6")

def cantidadDeDigitos(n):
    if n < 10:
        return 1
    else:
        return 1 + cantidadDeDigitos(n // 10)

print(f'Digitos de 333: {cantidadDeDigitos(333)}')

# //////// Ejercicio 7 ////////
print("\nEjercicio 7")

def esPotencia(n, b):
    if n == 1 or n == 0 or b * b == n:
        return True
    elif b * b > n:
        return False
    else:
        return esPotencia(n - b * b, b)

print(f"esPotencia(8, 2): {esPotencia(8, 2)}")
print(f"esPotencia(16, 2): {esPotencia(16, 2)}")
print(f"esPotencia(64, 4): {esPotencia(64, 4)}")
print(f"esPotencia(70, 10): {esPotencia(70, 10)}")
print(f"esPotencia(1, 2): {esPotencia(1, 2)}")
print(f"esPotencia(144, 12): {esPotencia(144, 12)}")

def esPotencia(n,b):
    return True if n==1 else False if n<b else esPotencia(n/b,b)

# //////// Ejercicio 8 ////////
print("\nEjercicio 8")

def posiciones(a, b, l=None, indice=0):
    if l is None:
        l = []
    if b in a[indice:]:
        indice = a.finde(b,indice)
        l.append(indice)
        return posiciones(a, b, l, indice + len(b))
    else:
        return 1

# //////// Ejercicio 13 ////////
print("\nEjercicio 13")


def combinaciones(lista, k):
    def distributiva(l0, l1):
        return [e1 + e0 for e1 in l1 for e0 in l0]

    def combina(l, k):
        return l if k == 1 else distributiva(l, (combina(l, k - 1)))

    print(" ".join(combina(lista, k)))


if __name__ == "__main__":
    # Aclaraci�n: Si bien la funci�n se llama combinaciones en realidad
    # se trata de una Variaci�n con Repetici�n. El n�mero total de elementos
    # generados ser� Vr=len(lista)**k
    combinaciones(["a", "b", "c"], 4)

