# //////// Ejercicio 1 ////////
print("\nEjercicio 1")

def sumaTupla(tupla):
    suma = sum(tupla)
    return suma


mi_tupla = (1, 2, 3, 4, 5)
resultado = sumaTupla(mi_tupla)
print(resultado)  # Esto imprimirá 15, que es la suma de los números en la tupla

# //////// Ejercicio 2 ////////
print("\nEjercicio 2")

def minMax(tupla):
    return min(tupla) + max(tupla)

def main():
    tupla = (1, 2, 3, 4, 5)
    print(minMax(tupla))

if __name__ == "__main__":
    main()

# //////// Ejercicio 3 ////////
print("\nEjercicio 3")

def todosNumeros(tupla):
    return all(isinstance(item, int) for item in tupla)

tupla_1 = (1, 2, 3, 4)
tupla_2 = (1, 2, '3', 4)

resultado_1 = todosNumeros(tupla_1)
resultado_2 = todosNumeros(tupla_2)

print(resultado_1)  # Esto imprimirá True
print(resultado_2)  # Esto imprimirá False

# //////// Ejercicio 4 ////////
print("\nEjercicio 4")

def tipoDominante(lista):
    def tipos(lista):
        return [
            (0, len([t for t in lista if type(t) == type(True)])),
            (1, [str(type(t))[8:-2] for t in lista].count("int")),
            (2, [str(type(t))[8:-2] for t in lista].count("float")),
            (3, [str(type(t))[8:-2] for t in lista].count("str")),
        ]

    # print(tipos(lista))
    def func(l):
        if len(l) != 1:
            raise TypeError
        return l[0][0]

    def dominante(l):
        return [(x, y) for x, y in l if y >= sorted(l, reverse=True, key=lambda x: x[1])[0][1]]

    return func(dominante(tipos(lista)))


if __name__ == "__main__":
    print(tipoDominante([1, "a", 0.5, True, 2, True, True, True, True]))

# //////// Ejercicio 10 ////////
print("\nEjercicio 10")

def butlast(n, l):
    if n >= len(l):
        return []
    else:
        return [l[0], ] + butlast(n, l[1::])

print(butlast(2, [1, 2, 3, 4, 5, 6]))
print(butlast(2, [1, 2]))
print(butlast(2, [1, ]))
print(butlast(1, [1, 2]))
print(butlast(3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, ]))

# //////// Ejercicio 12 ////////
print("\nEjercicio 12")

def remove_if(p, l):
    # Usa la funcion filter para iterar sobre la lista l y llamar a la función p() con cada elemento
    return list(filter(lambda x: not p(x), l))

def capicua(s):
    return s == s[::-1]

lista = ["ana", "juan", "pepe", "jose", "maria", "luisa", "pedro", "ana"]

print(remove_if(capicua, lista))

# //////// Ejercicio 17 ////////
print("\nEjercicio 17")

print("Función 1")
doble = lambda x: x * 2
print("Mostrando resultado")
print(doble(3), "\n")

print("Función 2")
impar = lambda x: x % 2 != 0
print("Mostrando resultado")
print(impar(3), "\n")

print("Función 3")
mayor = lambda x, y: x if len(x) > len(y) else y
print("Mostrando resultado")
print(mayor("Ana", "Pablo"), "\n")

print("Función 4")
duplicar_dupla = lambda x, y: (x * 2, y * 3)
print("Mostrando resultado")
print(duplicar_dupla(3, 4), "\n")

print("Función 5")
mayor_que_0 = lambda x: x > 0
print("Mostrando resultado")
print(mayor_que_0(3), "\n")

print("Función 6")
rango = lambda x, y, z: True if x >= y and x <= z else False
print("Mostrando resultado")
print(rango(11, 1, 10), "\n")

print("Función 7")
dentro_de_circunferencia = lambda x, y, r: x ** 2 + y ** 2 <= r ** 2
print("Mostrando resultado")
print(dentro_de_circunferencia(2, 2, 3), "\n")

print("Función 8")
area_triangulo = lambda b, h: (b * h) / 2
print("Mostrando resultado")
print(area_triangulo(3, 4), "\n")

print("Función 9")
area_cuadrado = lambda l: l ** 2
print("Mostrando resultado")
print(area_cuadrado(3), "\n")

print("Función 10")
ascendente = lambda l: sorted(l)
descendente = lambda l: sorted(l, reverse=True)
print("Mostrando resultado")
lista = [3, 4, 1, 2, 5]
print(ascendente(lista), "\n")
print(descendente(lista), "\n")

# //////// Ejercicio 29 ////////
print("\nEjercicio 29")

class Contador:
    def _init_(self,max=1):
        self.max=max
        self.contador=0

    def _iter_(self):
        return self

    def _next_(self):
        self.contador=(self.contador+1) % self.max
        return self.contador

c=Contador(5)
i=iter(c)
print(list(i))
for j in range(2):
    print(next(i))