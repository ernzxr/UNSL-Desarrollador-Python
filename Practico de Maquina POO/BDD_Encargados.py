from Encargado import Encargado

class BDD_Encargados:
    def __init__(self):
        self.__data = []
        self.__index = 0

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index < len(self.__data):
            encargado = self.__data[self.__index]
            self.__index += 1
            return encargado
        else:
            raise StopIteration

    def formatearArchivo(self):
        with open("Encargados.txt", "r") as archivo:
            for linea in archivo:
                nombre, dni = linea.strip().split(",")
                encargado = Encargado(nombre, dni)
                self.__data.append(encargado)

    def validarIngreso(self):
        def error():
            while True:
                print("Seleccione una opcion: ")
                print("[1] Intentar nuevamente")
                print("[0] Volver")
                opcion = input("Opcion: ")
                if opcion == "1":
                    return self.validarIngreso()
                elif opcion == "0":
                    return False
                else:
                    print("Ingrese una opcion valida.\n")

        encargado = None
        inputDNI = input("\n1. Ingrese su DNI sin puntos: ")

        for BDD_encargado in self.__data:
            if BDD_encargado.dni == inputDNI:
                encargado = BDD_encargado
                break

        if encargado:
            inputNombre = input("2. Ingrese su nombre completo: ")
            if encargado.nombre == inputNombre:
                print(f"Acceso concedido.")
                print(f"\nBienvenido {encargado.nombre}!.")
                return encargado
            else:
                print("Ingreso invalido!\n")
                return error()
        else:
            print("El DNI ingresado no existe!\n")
            return error()