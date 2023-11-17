# //////// Ejercicio 6 ////////
print("\nEjercicio 6")

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def getNombre(self):
        return self.nombre

    def setNombre(self, newNombre):
        self.nombre = newNombre

    def getEdad(self):
        return self.edad

    def setEdad(self, newEdad):
        self.edad = newEdad

# //////// Ejercicio 7 ////////
print("\nEjercicio 7")

class EmpleadoPorHora:
    def __init__(self, nombre, trabajo, precio, horas):
        self.nombre = nombre
        self.trabajo = trabajo
        self.precio = precio
        self.horas = horas

    def getNombre(self):
        return self.nombre

    def setNombre(self, newNombre):
        self.nombre = newNombre

    def getTrabajo(self):
        return self.trabajo

    def setTrabajo(self, newTrabajo):
        self.trabajo = newTrabajo

    def getPrecio(self):
        return self.precio

    def setPrecio(self, newPrecio):
        self.precio = newPrecio

    def getHoras(self):
        return self.horas

    def setHoras(self, newHoras):
        self.horas = newHoras

# //////// Ejercicio 8 ////////
print("\nEjercicio 8")

class EmpleadoExclusivo:
    def __init__(self, nombre, trabajo, sueldo):
        self.nombre = nombre
        self.trabajo = trabajo
        self.sueldo = sueldo

    def getNombre(self):
        return self.nombre

    def setNombre(self, newNombre):
        self.nombre = newNombre

    def getTrabajo(self):
        return self.trabajo

    def setTrabajo(self, newTrabajo):
        self.trabajo = newTrabajo

    def getSueldo(self):
        return self.sueldo

    def setSueldo(self, newSueldo):
        self.sueldo = newSueldo

# //////// Ejercicio 5 ////////
print("\nEjercicio 5")

def main():
    n = int(input("Ingrese la cantidad de personas a ingresar en la lista: "))

    for i in range(n):

if __name__ == "__main__":
    main()