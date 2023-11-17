class Profesor:
    def __init__(self, nombre, materia, curso, division):
        self.__nombre = nombre
        self.__materia = materia
        self.__curso = curso
        self.__division = division

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def materia(self):
        return self.__materia

    @materia.setter
    def materia(self, materia):
        self.__materia = materia

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso):
        self.__curso = curso

    @property
    def division(self):
        return self.__division

    @division.setter
    def division(self, division):
        self.__division = division

    def verNota(self, alumnosBDD):
        alumno = alumnosBDD.validarAlumno()

        if alumno:
            print(f"Alumno: {alumno.nombre} - Calificacion: {alumno.nota}")

    def cargarNota(self, alumnosBDD):
        alumno = alumnosBDD.validarAlumno()

        if alumno:
            while True:
                if alumno.nota == -1:
                    try:
                        nuevaNota = int(input("2. Ingrese la calificacion del Alumno: "))
                        if 0 <= nuevaNota <= 10:
                            alumno.nota = nuevaNota
                            alumnosBDD.actualizarArchivo()
                            print("Nota cargada!")
                            return
                        else:
                            print("La nota ingresada no es valida! (0 a 10)\n")
                    except:
                        print("La nota debe ser un valor numerico!\n")
                else:
                    print("La nota ya ha sido cargada! seleccione la opcion de modificar nota desde el menu.")
                    return

    def modificarNota(self, alumnosBDD):
        alumno = alumnosBDD.validarAlumno()

        if alumno:
            while True:
                if alumno.nota != -1:
                    try:
                        nuevaNota = int(input("2. Ingrese la calificacion del Alumno: "))
                        if 0 <= nuevaNota <= 10:
                            alumno.nota = nuevaNota
                            alumnosBDD.actualizarArchivo()
                            print("Nota modificada!")
                            return
                        else:
                            print("La nota ingresada no es valida! (0 a 10)\n")
                    except:
                        print("La nota debe ser un valor numerico!\n")
                else:
                    print("La nota aun no se ha cargado, debe ser cargada antes de ser modificada.")
                    return

    def eliminarNota(self, alumnosBDD):
        alumno = alumnosBDD.validarAlumno()

        if alumno:
            if alumno.nota != -1:
                alumno.nota = -1
                alumnosBDD.actualizarArchivo()
                print("Se ha eliminado la nota del alumno.")
                return
            else:
                print("La nota ya se encontraba sin cargar.")
                return
