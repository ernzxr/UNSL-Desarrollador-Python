# //////// Ejercicio 11 ////////
print("\nEjercicio 11")

class Animal:
    def __init__(self, grupoAnimal):
        self.grupoAnimal = grupoAnimal

    def getGrupoAnimal(self):
        return self.grupoAnimal

    def setGrupoAnimal(self, newGrupoAnimal):
        self.grupoAnimal = newGrupoAnimal

class Perro(Animal):
    def __init__(self, grupoAnimal, raza):
        super().__init__(grupoAnimal)
        self.raza = raza

    def getRaza(self):
        return self.raza

    def setRaza(self, newRaza):
        self.raza = newRaza

class Pez(Animal):
    def __init__(self, grupoAnimal, tipoAgua):
        super().__init__(grupoAnimal)
        self.tipoAgua = tipoAgua

    def getTipoAgua(self):
        return self.tipoAgua

    def setTipoAgua(self, newTipoAgua):
        self.tipoAgua = newTipoAgua

def ejercicio11():
    animales = []

    n = int(input("Ingrese la cantidad de peces a agregar: "))

    for i in range(n):
        tipo = input(f"{i+1}. Ingrese el tipo de agua del pez: ")
        animales.append(Pez("Vertebrado", tipo))

    n = int(input("Ingrese la cantidad de perros a agregar: "))

    for i in range(n):
        razaPerro = input(f"{i + 1}. Ingrese la raza del perro: ")
        animales.append(Perro("Vertebrado", razaPerro))

    for animal in animales:
        if isinstance (animal, Perro):
            print(f"Animal: Perro - Grupo: {animal.getGrupoAnimal()} - Raza: {animal.getRaza()}")
        elif isinstance (animal, Pez):
            print(f"Animal: Pez - Grupo: {animal.getGrupoAnimal()} - Tipo de Agua: {animal.getTipoAgua()}")

ejercicio11()

# //////// Ejercicio 12 ////////
print("\nEjercicio 12")

class ContadorLimitado:
    def __init__(self, maximo, numero):
        self.maximo = maximo
        self.inicializacion = self.validarInicializacion(numero)

    def getValorActual(self):
        return self.inicializacion

    def setIncrementar(self):
        if self.inicializacion == self.maximo:
            print(f"Valor maximo alcanzado: {self.maximo}")
        else:
            self.inicializacion += 1
            print(self.getValorActual())

    def validarInicializacion(self, numero):
        if numero >= self.maximo:
            print("El valor ingresado supera el maximo permitido.")
            print("Se inicializa el programa en 0.")
            return 0
        else:
            return numero

    def __repr__(self):
        return f"ContadorLimitado({self.maximo}, {self.inicializacion})"

def ejercicio12():
    contador = ContadorLimitado(5, 0)
    print (contador.__repr__())
    print(contador.getValorActual())
    for i in range(6):
        contador.setIncrementar()

ejercicio12()

# //////// Ejercicio 13 ////////
print("\nEjercicio 13")

class AnimalDos:
    def __init__(self, nombre):
        self.nombre = nombre

class Vertebrado(AnimalDos):
    pass

class Invertebrado(AnimalDos):
    pass

class Ave(Vertebrado):
    pass

class Mamifero(Vertebrado):
    pass

class Anfibio(Vertebrado):
    pass

class Reptil(Vertebrado):
    pass

class PezDos(Vertebrado):
    pass

class Artropodo(Invertebrado):
    def __init__(self, nombre, tipo):
        super().__init__(nombre)
        self.tipo = tipo

class Anelido(Invertebrado):
    def __init__(self, nombre, tipo):
        super().__init__(nombre)
        self.tipo = tipo

class Molusco(Invertebrado):
    def __init__(self, nombre, tipo):
        super().__init__(nombre)
        self.tipo = tipo

class Porifero(Invertebrado):
    def __init__(self, nombre, tipo):
        super().__init__(nombre)
        self.tipo = tipo

class Cnidario(Invertebrado):
    def __init__(self, nombre, tipo):
        super().__init__(nombre)
        self.tipo = tipo

class Equinodermo(Invertebrado):
    def __init__(self, nombre, tipo):
        super().__init__(nombre)
        self.tipo = tipo

class Nematodo(Invertebrado):
    def __init__(self, nombre, tipo):
        super().__init__(nombre)
        self.tipo = tipo

class Platelminto(Invertebrado):
    def __init__(self, nombre, tipo):
        super().__init__(nombre)
        self.tipo = tipo

