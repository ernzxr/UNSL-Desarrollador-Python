# //////// Ejercicio 10 ////////
print("\nEjercicio 10")

def butlast(n, l):
    if n >= len(l):
        return []
    else:
        return [l[0]] + butlast(n, l[1::])

print(f"butlast(4, [1, 2, 3, 4, 5]): {butlast(4, [1, 2, 3, 4, 5])}")
print(f"butlast(4, [1, 2]): {butlast(4, [1, 2])}")

# //////// Ejercicio 12 ////////
print("\nEjercicio 12")

def remove_if(p, l):
    return list(filter(lambda x: not p(x), l))

def capicua(s):
    return s == s[::-1]

lista = ["ana", "pepe", "radar", "neuquen", "ernes"]

print(f"Lista: {lista}")
print(f"Lista sin capicuas: {remove_if(capicua, lista)}")

# //////// Ejercicio 15 ////////
print("\nEjercicio 15")

lambdaFunction = lambda x, y: x if x > y else y if y > x else x

print(f"lambdaFunction(2,2): {lambdaFunction(2,2)}")
print(f"lambdaFunction(3,2): {lambdaFunction(3,2)}")
print(f"lambdaFunction(2,4): {lambdaFunction(2,4)}")

# //////// Ejercicio 17 ////////
print("\nEjercicio 17")

lambdaDoble = lambda x: x * 2
print(f"1. lambdaDoble(2): {lambdaDoble(2)}")

lambdaImpar = lambda x: x % 2 != 0
print(f"2. lambdaImpar(2): {lambdaImpar(2)}")

lambdaStringLargo = lambda x, y: x if len(x) > len(y) else y if len(x) < len(y) else y + " y " + x
print(f"3. lambdaStringLargo('Ernesto', 'Lucas'): {lambdaStringLargo('Ernesto', 'Lucas')}")
print(f"3. lambdaStringLargo('Gatitos', 'Perrito'): {lambdaStringLargo('Gatitos', 'Perrito')}")

lambdaDupla = lambda x: (x[0]*2, x[1]*3)
print(f"4. lambdaDupla((2,2)): {lambdaDupla((2,2))}")

lambdaPositivo = lambda x: x > 0
print(f"5. lambdaPositivo(1): {lambdaPositivo(1)}")
print(f"5. lambdaPositivo(0): {lambdaPositivo(0)}")

lambdaRango10_20 = lambda x: 10 < x < 20
print(f"6. lambdaRango10_20(11): {lambdaRango10_20(11)}")
print(f"6. lambdaRango10_20(22): {lambdaRango10_20(22)}")

lambdaCircuferencia = lambda x, y, r: x ** 2 + y ** 2 <= r ** 2
print(f"7. lambdaCircuferencia(2, 2, 3): {lambdaCircuferencia(2, 2, 3)}")

lambdaAreaTriangulo = lambda x, y: (x * y) / 2
print(f"8. lambdaAreaTriangulo(5,10): {lambdaAreaTriangulo(5,10)} cms")

lambdaAreaCuadrado = lambda x: x * x
print(f"9. lambdaAreaCuadrado(4): {lambdaAreaCuadrado(4)} cms")

lambdaOrdenar = lambda x: sorted(x)
print(f"9. lambdaOrdenar([1,3,2,4]): {lambdaOrdenar([1,3,2,4])}")
print(f"9. lambdaOrdenar([1,3,2,4]): {lambdaOrdenar([1,3,2,4])[::-1]}")

# //////// Ejercicio 18 ////////
print("\nEjercicio 18")

def funcionStringMayusculas():
    return lambda x: x.upper()

textoMayusculas = funcionStringMayusculas()

print(f"textoMayusculas('Hola'): {textoMayusculas('Hola')}")

# //////// Ejercicio 24 ////////
print("\nEjercicio 24")

def generarArea(valor, x, y):
    return (x * y) / 2 if valor else x * y

t1 = generarArea(True,2,3)
r1 = generarArea(False,2,2)

print("Área del Triángulo:", t1, "cms")
print("Área del Rectángulo:", r1, "cms")

# //////// Ejercicio 29 ////////
print("\nEjercicio 29")

class ContadorModulo:
    def __init__(self, n):
        self.iterable = [i for i in range(0, n)]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable):
            nextIterable = self.iterable[self.index]
            self.index += 1
            return nextIterable
        else:
            self.index = 0
            return self.iterable[self.index]

    def next(self):
        if self.index < len(self.iterable):
            nextIterable = self.iterable[self.index]
            self.index += 1
            return nextIterable
        else:
            self.index = 0
            return self.iterable[self.index]

c = ContadorModulo(3)
i = iter(c)

print(f"next(i): {next(i)}")
print(f"next(i): {next(i)}")
print(f"next(i): {next(i)}")
print(f"next(i): {next(i)}")

print(f"\nc.next(): {c.next()}")
print(f"c.next(): {c.next()}")
print(f"i.next(): {i.next()}")
print(f"i.next(): {i.next()}")