# //////// Ejercicio 11 ////////
print("\nEjercicio 11")

class Animal:
    animales = []

    def __init__(self, grupoAnimal):
        self.grupoAnimal = grupoAnimal
        Animal.animales.append(self)

    def getGrupoAnimal(self):
        return self.grupoAnimal

    def setGrupoAnimal(self, newGrupoAnimal):
        self.grupoAnimal = newGrupoAnimal

    @staticmethod
    def getAnimales():
        return Animal.animales

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
    n = int(input("Ingrese la cantidad de peces a agregar: "))

    for i in range(n):
        tipo = input(f"{i+1}. Ingrese el tipo de agua del pez: ")
        Pez("Vertebrado", tipo)

    n = int(input("Ingrese la cantidad de perros a agregar: "))

    for i in range(n):
        razaPerro = input(f"{i + 1}. Ingrese la raza del perro: ")
        Perro("Vertebrado", razaPerro)

    print(Animal.getAnimales())

    for animal in Animal.getAnimales():
        if isinstance (animal, Perro):
            print()
        elif isinstance (animal, Pez):
            pass

ejercicio11()

# //////// Ejercicio 12 ////////
print("\nEjercicio 12")

class ContadorLimitado:
    def __init__(self, numero):
        self.maximo = 10
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

def ejercicio12():
    contador = ContadorLimitado(11)
    print(contador.getValorActual())
    for i in range(11):
        contador.setIncrementar()

ejercicio12()

# //////// Ejercicio 13 ////////
print("\nEjercicio 13")

class AnimalDos:
    def __init__(self, nombre):
        self.nombre = nombre

class Vertebrado(Animales):
    pass

class Invertebrado(Animales):
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

# //////// Ejercicio 14 ////////
print("\nEjercicio 14")

class Empresa:
    def __init__(self, nombre, direccion, cuit):
        self.nombre = nombre
        self.direccion = direccion
        self.cuit = cuit

    def getNombreEmpresa(self):
        return self.nombre

    def getDireccionEmpresa(self):
        return self.direccion

    def getCuit(self):
        return self.cuit

class RenglonDeFactura:
    def __init__(self, unidades, descripcion, precio):
        self.unidades = int(unidades)
        self.descripcion = descripcion
        self.precio = int(precio)
        self.total = int(precio) * int(unidades)

    def getDescripcion(self):
        return self.descripcion

    def getTotal(self):
        return self.total

class Factura:
    def __init__(self, numeroFactura, empresa, renglones):
        self.numeroFactura = numeroFactura
        self.empresa = empresa
        self.renglones = renglones

    def getEmpresa(self):
        return self.empresa

    def totalSinIva(self):
        total = 0
        for renglon in self.renglones:
            total += renglon.getTotal()
        return total

    def porcentajeIva(self):
        total = 0
        for renglon in self.renglones:
            total += renglon.getTotal()
        return total * 0.21

    def totalConIva(self):
        return self.totalSinIva() + self.porcentajeIva()

def ejercicio14():
    facturas = {}

    cantidadFacturas = int(input("\nIngrese la cantidad de facturas a cargar: "))

    for i in range(cantidadFacturas):
        cargarFactura = []

        numeroDeFactura = input(f"\n{i + 1}. Ingrese el numero de factura: ")

        nombreEmpresa = input("Ingrese el nombre de la empresa: ")
        direccionEmpresa = input("Ingrese la direccion de la empresa: ")
        cuitEmpresa = input("Ingrese el CUIT de la empresa: ")
        empresa = Empresa(nombreEmpresa, direccionEmpresa, cuitEmpresa)

        cantidadRenglones = int(input("\nCuantos renglones tiene la factura?: "))

        for j in range(cantidadRenglones):
            print(f"\nRenglon: {j + 1}")
            descripcionRenglon = input("Ingrese el nombre del producto: ")
            precioRenglon = input("Ingrese el precio unitario: ")
            unidadesRenglon = input("Ingrese las unidades vendidas: ")
            cargarFactura.append(RenglonDeFactura(unidadesRenglon, descripcionRenglon, precioRenglon))

        facturas[numeroDeFactura] = Factura(numeroDeFactura, empresa, cargarFactura)

    maximoComprador = 0
    maximoCompradorNombre = ""
    cantidadFacturasEmitidas = 0
    importeTotalDeVentas = 0

    for factura in facturas.values():
        importeTotalDeVentas += factura.totalConIva()
        cantidadFacturasEmitidas += 1
        if (factura.totalSinIva() > maximoComprador):
            maximoComprador = factura.totalSinIva()
            maximoCompradorNombre = factura.getEmpresa().getNombreEmpresa()

    print(f"\nCantidad de facturas emitidas: {cantidadFacturasEmitidas}")
    print(f"Importe total de las ventas con IVA: ${importeTotalDeVentas}")
    print(f"El maximo comprador fue la empresa {maximoCompradorNombre} con un importe de ${maximoComprador} sin IVA\n")

    for numeroFactura in facturas.keys():
        print(f"Numero de factura: {numeroFactura}")

ejercicio14()