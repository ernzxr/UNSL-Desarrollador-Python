class PilaDeEnteros:
    def __init__(self):
        self.__pila=[]

    def push(self, elemento):
        if type(elemento)==int:
            self.__pila.append(elemento)
        else:
            raise TypeError("La Pila es de Enteros")
        return

    def pop(self):
        return self.__pila.pop()

    def top(self):
        return self.__pila[-1]

    def empty(self):
        return len(self.__pila)==0

    def __str__(self):
        return str(self.__pila)

    def longitud(self):
        return len(self.__pila)

    def full(self):
        raise TypeError("Una Pila en Python no se llena")

    def __add__(self, other):
        self.__pila.append(other)

    def __getPila(self):
        return self.__pila

    def __eq__(self, other):
        return self.__pila==other.__getPila()

    def __neg__(self):
        return self.__pila.pop()

# creacion de objetos
p=PilaDeEnteros()
q=PilaDeEnteros()

# utilizacion de operador + y metodo
print(f"Pila vacia: {p}")
p.push(12)
p+5
p+3
print(f"Pila luego de utilizar operador + y metodo push: {p}")

# utilizacion de operador -
-p
print(f"Pila luego de utilizar operador -: {p}")

# metodo longitud()
print(f"Longitud de la Pila: {p.longitud()}")

# comparacion de pilas
print(f"Pila p = {p} y pila q = {q}")
print(f"Comparacion pila p == q: {p == q}")

# representacion string de pila
print(f"Representacion string de pila p: {p}")