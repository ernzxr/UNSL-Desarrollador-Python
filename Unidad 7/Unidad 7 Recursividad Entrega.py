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

#def esPotencia(n,b):
#    return True if n==1 else False if n<b else esPotencia(n/b,b)

# //////// Ejercicio 15 ////////
print("\nEjercicio 15")

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.children = []

    def recorridoSimetrico(self):
        result = []

        # Recorrer el primer hijo en simétrico
        if self.children:
            result.extend(self.children[0].recorridoSimetrico())

        # Agregar el valor del nodo actual al resultado
        result.append(self.valor)

        # Recorrer los hijos restantes en simétrico
        for i in range(1, len(self.children)):
            result.extend(self.children[i].recorridoSimetrico())

        return result

    def recorridoPostOrden(self):
        result = []

        # Recorrer los hijos en postorden
        for child in self.children:
            result.extend(child.recorridoPostOrden())

        # Agregar el valor del nodo actual al resultado
        result.append(self.valor)

        return result

    def recorridoPreOrden(self):
        result = []

        # Agregar el valor del nodo actual al resultado
        result.append(self.valor)

        # Recorrer los hijos en preorden
        for child in self.children:
            result.extend(child.recorridoPreOrden())

        return result

root = Nodo(1)
root.children.append(Nodo(2))
root.children.append(Nodo(3))
root.children.append(Nodo(4))
root.children[0].children.append(Nodo(5))
root.children[0].children.append(Nodo(6))
root.children[1].children.append(Nodo(7))
root.children[2].children.append(Nodo(8))

print(f"Orden Simetrico: {root.recorridoSimetrico()}")
print(f"Post Orden: {root.recorridoPostOrden()}")
print(f"Pre Orden: {root.recorridoPreOrden()}\n")

root.children[2].children.append(Nodo(9))
print(f"Orden Simetrico: {root.recorridoSimetrico()}")
print(f"Post Orden: {root.recorridoPostOrden()}")
print(f"Pre Orden: {root.recorridoPreOrden()}")

# pude entender la teoria de los ordenes y diagramarlo en la imagen que adjunte complementariamente a la entrega
# no obstante no pude resolver el problema solo, tuve que acudir a chatgtp para que me de una mano
# siento que el ejercicio se pudo resolver de otra manera alternativa pero no logré descubrir como.