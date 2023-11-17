from Profesor import Profesor

class BDD_Profesores:
    def __init__(self):
        self.__data = []
        self.__index = 0

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index < len(self.__data):
            profesor = self.__data[self.__index]
            self.__index += 1
            return profesor
        else:
            raise StopIteration
    def formatearArchivo(self):
        with open("Profesores.txt", "r") as archivo:
            for linea in archivo:
                nombre, materia, curso, division = linea.strip().split(",")
                profesor = Profesor(nombre, materia, curso, division)
                self.__data.append(profesor)

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

        profesor = None
        inputNombre = input("\n1. Ingrese su nombre completo: ")

        for BDD_profesor in self.__data:
            if BDD_profesor.nombre == inputNombre:
                profesor = BDD_profesor
                break

        if profesor:
            inputMateria = input("2. Materia que dicta: ")
            inputCurso = input("3. Curso: ")
            inputDivision = input("4. Division: ")
            if profesor.materia == inputMateria and profesor.curso == inputCurso and profesor.division == inputDivision:
                print(f"Acceso concedido.")
                print(f"\nBienvenido {profesor.nombre}!.")
                return profesor
            else:
                print("Ingreso invalido!\n")
                return error()
        else:
            print("El profesor ingresado no existe!\n")
            return error()

    def validarMateriaAlumno(self, materia):
        for BDD_profesor in self.__data:
            if BDD_profesor.materia == materia:
                return True

        print(f"La materia ingresada no esta disponible.\n")
        return False

    def validarProfesorAlumno(self, materia, profesor):
        for BDD_profesor in self.__data:
            if BDD_profesor.nombre == profesor and BDD_profesor.materia == materia:
                return True

        for BDD_profesor in self.__data:
            if BDD_profesor.nombre == profesor:
                print(f"El profesor ingresado no dicta la materia {materia}.\n")
                return False

        print("El profesor ingresado no se encuentra en sistema.\n")
        return False

    def validarCursoAlumno(self, materia, profesor, curso):
        for BDD_profesor in self.__data:
            if BDD_profesor.nombre == profesor and BDD_profesor.materia == materia and BDD_profesor.curso == curso:
                return True

        print(f"No existe el curso {curso} para el profesor {profesor} en la materia {materia}.\n")
        return False

    def validarDivisionAlumno(self, materia, profesor, curso, division):
        for BDD_profesor in self.__data:
            if BDD_profesor.nombre == profesor and BDD_profesor.materia == materia and BDD_profesor.curso == curso and BDD_profesor.division == division:
                return True

        print(f"No existe la division {division} para el profesor {profesor} en la materia {materia} del curso {curso}.\n")
        return False
