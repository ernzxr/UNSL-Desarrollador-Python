# //////// Ejercicio 3 ////////
import functools

print("\nEjercicio 3")

paises = ["Estonia", "Finlandia", "Suiza", "Dinamarca", "Noruega", "Islandia"]
nombres = ["Carlos", "Daniel", "Alberto", "Luis"]
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1.
paisesMayuscula = list(map(lambda x:x.upper(), paises))
print(f"list(map(lambda x:x.upper(), paises)):\n{paisesMayuscula}\n")

# 2.
cuadradoNumeros = list(map(lambda x:x**2, numeros))
print(f"list(map(lambda x:x**2, numeros)):\n{cuadradoNumeros}\n")

# 3.
nombresMayuscula = list(map(lambda x:x.upper(), nombres))
print(f"list(map(lambda x:x.upper(), nombres)):\n{nombresMayuscula}\n")

# 4.
filtroPaisesN = list(filter(lambda x: "n" in x.lower(), paises))
print(f"list(filter(lambda x: 'n' in x.lower(), paises)):\n{filtroPaisesN}\n")

# 5.
filtroPaisesLen = list(filter(lambda x: len(x)>6, paises))
print(f"list(filter(lambda x: len(x)>6, paises)):\n{filtroPaisesLen}\n")

# 6.
filtroPaisesE = list(filter(lambda x: "e" in x.lower(), paises))
print(f"list(filter(lambda x: 'e' in x.lower(), paises)):\n{filtroPaisesE}\n")

# 7.
def recuperarString(l):
    return list(filter(lambda x: type(x) == str, l))

print(f"recuperarString([1, '2', 'tres', 4]):\n{recuperarString([1, '2', 'tres', 4])}\n")

# 8.
sumarNumeros = functools.reduce(lambda a, b: a+b, numeros)
print(f"Suma con reduce de {numeros}:\n{sumarNumeros}\n")

# 9.
PNE = ["Noruega", "Finlandia", "Suecia", "Islandia", "Dinamarca", "Estonia", "Lituania", "Letonia"]

paisesEuropa = functools.reduce(lambda a, b: a + ", " + b, filter(lambda pais: pais in PNE, paises))
print(f"Paises del Norte de Europa:\n{paisesEuropa}")

# //////// Ejercicio 4 ////////
print("\nEjercicio 4")

listaDupla = [(0, 'a'), (4, 'c'), (2, 'd'), (7, 'b')]

print(f"Mostrando la lista de duplas:\n{listaDupla}\n")

listaDupla.sort(key = lambda dupla: dupla[0])
print(f"Mostrando lista de duplas ordenada por numero:\n{listaDupla}\n")

listaDupla.sort(key = lambda dupla: dupla[1])
print(f"Mostrando lista de duplas ordenada por letra:\n{listaDupla}")

# //////// Ejercicio 5 ////////
print("\nEjercicio 5")

def sumarSi(f, l):
    return sum(filter(f,l))

susi = sumarSi(lambda x:x % 2 != 0, numeros)
print(f"sumarSi(lambda x:x % 2 != 0, {numeros}):\n{susi}")

# //////// Ejercicio 7 ////////
print("\nEjercicio 7")

def crearPotencia(exponente):
    def potenciaDeDos():
        return 2**exponente
    return potenciaDeDos

dosAlCuadrado = crearPotencia(2)
print(f"dosAlCuadrado():\n{dosAlCuadrado()}")

# //////// Ejercicio 9 ////////
print("\nEjercicio 9")

def sumaTriupla(l):
    return list(map(sum,l))

print(f"sumaTriupla([(1,3,-1), (2,1,3), (5,3,2)]):\n{sumaTriupla([(1,3,-1), (2,1,3), (5,3,2)])}")