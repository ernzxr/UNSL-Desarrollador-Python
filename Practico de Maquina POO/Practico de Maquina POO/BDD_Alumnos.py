from Inscripciones import Alumno

class BDD_Alumnos:
    def __init__(self):
        self.__data = []
        self.__index = 0

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index < len(self.__data):
            alumno = self.__data[self.__index]
            self.__index += 1
            return alumno
        else:
            raise StopIteration

    def formatearArchivo(self):
        with open("Inscripciones.txt", "r") as archivo:
            for linea in archivo:
                fecha, nombre, materia, profesor, curso, division, nota = linea.strip().split(",")
                alumno = Alumno(nombre, fecha, materia, profesor, curso, division, int(nota))
                self.__data.append(alumno)

    def agregarAlumno(self, nombre, fecha, materia, profesor, curso, division):
        alumno = Alumno(nombre, fecha, materia, profesor, curso, division, -1)
        self.__data.append(alumno)

    def eliminarAlumno(self, alumno):
        self.__data.remove(alumno)

    def actualizarArchivo(self):
        lineas = []

        for alumno in self.__data:
            datos = [alumno.fecha, alumno.nombre, alumno.materia, alumno.profesor, alumno.curso, alumno.division, str(alumno.nota)]
            lineaFormateada = ",".join(datos)+"\n"
            lineas.append(lineaFormateada)

        with open("Inscripciones.txt", "w") as archivo:
            archivo.writelines(lineas)

    def validarAlumno(self):
        def error():
            while True:
                print("Seleccione una opcion: ")
                print("[1] Intentar nuevamente")
                print("[0] Volver")
                opcion = input("Opcion: ")
                if opcion == "1":
                    return self.validarAlumno()
                elif opcion == "0":
                    return
                else:
                    print("Ingrese una opcion valida.\n")

        inputNombre = input("\n1. Ingrese el nombre del Alumno: ")

        for BDD_alumno in self.__data:
            if BDD_alumno.nombre == inputNombre:
                return BDD_alumno

        print(f"El alumno {inputNombre} no se encuentra en el sistema!\n")
        return error()

    def validarNombreAlumno(self, nombre):
        for BDD_alumno in self.__data:
            if BDD_alumno.nombre == nombre:
                print("El alumno ya se encuentra inscripto en el sistema.\n")
                return False
        return True
