# //////// Ejercicio 2 ////////
print("\nEjercicio 2")

def potenciasDeDos(n):
    return [x**2 for x in range(n)]

print(f"potenciasDeDos(10): {potenciasDeDos(10)}")

# //////// Ejercicio 5 ////////
print("\nEjercicio 5")

def filtrarPar(l):
    return [x for x in l if x%2!=0]

print(f"filtrarPar([1,2,3,4,5,6,7,8,9]): {filtrarPar([1,2,3,4,5,6,7,8,9])}")

# //////// Ejercicio 7 ////////
print("\nEjercicio 7")

def cubos():
    return [x**3 for x in range(10)]

print(f"cubos(): {cubos()}")

# //////// Ejercicio 9 ////////
print("\nEjercicio 9")

#def tablas():
#    return {i:[i*j for j in range(1,11)] for i in range(1,11)}

n=int(input("Ingrese un numero para hacer la tabla de multiplicar: "))

def tabla(n):
    return {i:n*i for i in range(1,11)}

print(tabla(n))

# //////// Ejercicio 11 ////////
print("\nEjercicio 11")

n=int(input("Ingrese un numero positivo para hacer un generador que devuelva palindromos desde 0 hasta ese numero: "))

def generadorPalindromo(n):
    return (palindromo for palindromo in range(n) if str(palindromo) == str(palindromo)[::-1])

print(f"Espacio del generador: {generadorPalindromo(n)}")
print(f"Lista: {list(generadorPalindromo(n))}")

# //////// Ejercicio 14 ////////
print("\nEjercicio 14")

num=int(input("Ingrese un numero para crear un generador con sus multiplos: "))

def genMultiplos(num):
    i = 1
    while True:
        yield num * i
        i += 1

n=int(input(f"Ingrese la cantidad de multiplos de {num} que desea ver: "))

def verMultiplos(generador, n):
    return [next(generador) for _ in range(1,n+1)]

print(verMultiplos(genMultiplos(num), n))

# //////// Ejercicio 16 ////////
print("\nEjercicio 16")

num=int(input("Ingrese un numero para crear un generador con sus divisores: "))

def divisores(num):
    i = 1
    while i<=num:
        if not num%i:
            yield i
        i += 1

n=int(input(f"Ingrese la cantidad de divisores de {num} que desea ver: "))

def verDivisores(generador, n):
    l=[]
    try:
        for _ in range(n):
            l.append(next(generador))
    except:
        return l

print(verDivisores(divisores(num), n))