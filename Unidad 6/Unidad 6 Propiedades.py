# //////// Ejercicio 1 ////////
print("\nEjercicio 1")

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, newNombre):
        self._nombre = newNombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, newEdad):
        self._edad = newEdad

ernesto = Persona("Ernesto", 28)

print(ernesto.nombre)

# //////// Ejercicio 2 ////////
print("\nEjercicio 2")

class Button:
    def __init__(self):
        self._estado = False

    @property
    def estado(self):
        if (self._estado):
            return "Presionado"
        else:
            return "Libre"

    @estado.setter
    def estado(self, newEstado):
        if newEstado:
            self._estado = True
        else:
            self._estado = False

boton = Button()

print(f"Primer estado: {boton.estado}")
boton.estado = True
print(f"Segundo estado: {boton.estado}")
boton.estado = False
print(f"Tercer estado: {boton.estado}")


# //////// Ejercicio 4 ////////
print("\nEjercicio 4")

class SemaforoBoton:

    def __init__(self, contador):
        self._rojo = False
        self._amarillo = False
        self._verde = False
        self._contador = 0

    @property
    def rojo(self):
        return self._rojo

    @property
    def amarillo(self):
        return self._amarillo

    @property
    def verde(self):
        return self._verde

    @property
    def contador(self):
        return self._contador


    @rojo.setter
    def rojo(self, estado):
        self._rojo = estado


    @amarillo.setter
    def amarillo(self, estado):
        self._amarillo = estado


    @verde.setter
    def verde(self, estado):
        self._verde = estado


    @contador.setter
    def contador(self, press):
        if self._contador % 6 == 0:
            self.rojo = True
        elif self._contador % 6 == 1:
            self.rojo = False
        elif self._contador % 6 == 2:
            self.verde = True
        elif self._contador % 6 == 3:
            self.verde = False
        elif self._contador % 6 == 4:
            self.amarillo = True
        elif self._contador % 6 == 5:
            self.amarillo = False

        self._contador += 1


def main():
    semaforo1 = SemaforoBoton(0)

    while True:
        pregunta = input("Quiere presionar boton? s/n: ")
        if pregunta == "s":
            semaforo1.contador = True
            print(f"El semaforo esta en: rojo {semaforo1.rojo}")
            print(f"El semaforo esta en: verde {semaforo1.verde}")
            print(f"El semaforo esta en: amarillo {semaforo1.amarillo}")
        elif pregunta == "n":
            break


if __name__ == "__main__":
    main()