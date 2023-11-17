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

print(f"Nombre: {ernesto.nombre} - Edad: {ernesto.edad}")

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

def main():
    boton = Button()

    finalizar = False

    print("Operando el Boton!")
    while finalizar != True:
        opcion = input('Ingrese "1" [Presionar] - "0" [Soltar] - "S" [Salir]: ')

        if opcion == "1":
            boton.estado = True
            print(f"Boton - Estado: {boton.estado}\n")
        elif opcion == "0":
            boton.estado = False
            print(f"Boton - Estado: {boton.estado}\n")
        elif opcion.lower() == "s":
            print("Fin del programa.")
            finalizar = True
        else:
            print("Ingrese una opcion valida.\n")

if __name__ == "__main__":
    main()