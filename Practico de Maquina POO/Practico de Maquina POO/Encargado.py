class Encargado:
    def __init__(self, nombre, dni):
        self.__nombre = nombre
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    def verAlumnos(self, alumnosBDD):
        alumnos = [alumno.nombre for alumno in alumnosBDD]
        nombres = ", ".join(alumnos)
        print("\nLista de alumnos: ")
        print(nombres)
    
    def ingresarNombreAlumno(self, alumnosBDD):
        def error(*args):
            while True:
                print("Seleccione una opcion: ")
                print("[1] Intentar Nuevamente")
                print("[0] Volver")
                opcion = input("Opcion: ")
                if opcion == "1":
                    return self.ingresarNombreAlumno(*args)
                elif opcion == "0":
                    return None
                else:
                    print("Ingrese una opcion valida.\n")

        inputNombre = input("\n1. Ingrese el nombre completo del alumno: ")
        validarNombre = alumnosBDD.validarNombreAlumno(inputNombre)

        if validarNombre:
            print(f"Nombre registrado.")
            return inputNombre
        else:
            return error(alumnosBDD)

    def ingresarFechaInscripcionAlumno(self):
        def error():
            while True:
                print("Seleccione una opcion: ")
                print("[1] Intentar Nuevamente")
                print("[0] Volver")
                opcion = input("Opcion: ")
                if opcion == "1":
                    return self.ingresarFechaInscripcionAlumno()
                elif opcion == "0":
                    return None
                else:
                    print("Ingrese una opcion valida.\n")

        while True:
            inputFecha = input("\n2. Ingrese la fecha de inscripcion en formato DD/MM/AA: ")
            try:
                dia, mes, anio = map(int, inputFecha.split("/"))
                if not (1 <= dia <= 31):
                    print("El dia ingresado esta fuera de un rango valido.\n")
                    raise
                if not (1 <= mes <= 12):
                    print("El mes ingresado esta fuera de un rango valido.\n")
                    raise
                if not (0 <= anio <= 99):
                    print("El año de inscripcion esta fuera de un rango valido.\n")
                    raise
                print(f"Fecha ingresada: {inputFecha}.")
                return inputFecha
            except:
                print("El formato ingresado es invalido.\n")
                return error()

    def ingresarMateriaAlumno(self, profesoresBDD):
        def error(*args):
            while True:
                print("Seleccione una opcion: ")
                print("[1] Intentar Nuevamente")
                print("[0] Volver")
                opcion = input("Opcion: ")
                if opcion == "1":
                    return self.ingresarMateriaAlumno(*args)
                elif opcion == "0":
                    return None
                else:
                    print("Ingrese una opcion valida.\n")

        inputMateria = input("\n3. Ingrese la materia que va a cursar: ")
        validarMateria = profesoresBDD.validarMateriaAlumno(inputMateria)

        if validarMateria:
            print("Materia registrada.")
            return inputMateria
        else:
            return error(profesoresBDD)

    def ingresarProfesorAlumno(self, materia, profesoresBDD):
        def error(*args):
            while True:
                print("Seleccione una opcion: ")
                print("[1] Intentar Nuevamente")
                print("[0] Volver")
                opcion = input("Opcion: ")
                if opcion == "1":
                    return self.ingresarProfesorAlumno(*args)
                elif opcion == "0":
                    return None
                else:
                    print("Ingrese una opcion valida.\n")

        inputProfesor = input("\n4. Ingrese el profesor: ")
        validarProfesor = profesoresBDD.validarProfesorAlumno(materia, inputProfesor)

        if validarProfesor:
            print("Profesor registrado.")
            return inputProfesor
        else:
            return error(materia, profesoresBDD)

    def ingresarCursoAlumno(self, materia, profesor, profesoresBDD):
        def error(*args):
            while True:
                print("Seleccione una opcion: ")
                print("[1] Intentar Nuevamente")
                print("[0] Volver")
                opcion = input("Opcion: ")
                if opcion == "1":
                    return self.ingresarCursoAlumno(*args)
                elif opcion == "0":
                    return None
                else:
                    print("Ingrese una opcion valida.\n")

        inputCurso = input("\n5. Ingrese el curso: ")
        validarCurso = profesoresBDD.validarCursoAlumno(materia, profesor, inputCurso)

        if validarCurso:
            print("Curso registrado.")
            return inputCurso
        else:
            return error(materia, profesor, profesoresBDD)

    def ingresarDivisionAlumno(self, materia, profesor, curso, profesoresBDD):
        def error(*args):
            while True:
                print("Seleccione una opcion: ")
                print("[1] Intentar Nuevamente")
                print("[0] Volver")
                opcion = input("Opcion: ")
                if opcion == "1":
                    return self.ingresarDivisionAlumno(*args)
                elif opcion == "0":
                    return None
                else:
                    print("Ingrese una opcion valida.\n")

        inputDivision = input("\n6. Ingrese la division: ")
        validarDivision = profesoresBDD.validarDivisionAlumno(materia, profesor, curso, inputDivision)

        if validarDivision:
            print("Division registrada.")
            return inputDivision
        else:
            return error(materia, profesor, curso, profesoresBDD)

    def inscribirAlumno(self, nombre, fecha, materia, profesor, curso, division, alumnosBDD):
        alumnosBDD.agregarAlumno(nombre, fecha, materia, profesor, curso, division)
        alumnosBDD.actualizarArchivo()
        print(f"\nSe ha inscripto al alumno {nombre} a la materia {materia}.")
        return

    def eliminarAlumno(self, alumnosBDD):
        alumno = alumnosBDD.validarAlumno()

        if alumno:
            print(f"Alumno {alumno.nombre} eliminado!")
            alumnosBDD.eliminarAlumno(alumno)
            alumnosBDD.actualizarArchivo()
            return

    def validarAlumno(self, alumnosBDD):
        return alumnosBDD.validarAlumno()

    def modificarNombreAlumno(self, alumno, alumnosBDD):
        def error(*args):
            while True:
                print("Seleccione una opcion: ")
                print("[1] Intentar Nuevamente")
                print("[0] Volver")
                opcion = input("Opcion: ")
                if opcion == "1":
                    return self.modificarNombreAlumno(*args)
                elif opcion == "0":
                    return
                else:
                    print("Ingrese una opcion valida.\n")

        inputNombre = input("\n1. Ingrese el nuevo nombre del alumno: ")
        validarNombre = alumnosBDD.validarNombreAlumno(inputNombre)

        if validarNombre:
            print(f"\nSe ha modificado el nombre correctamente a: {inputNombre}.")
            alumno.nombre = inputNombre
            alumnosBDD.actualizarArchivo()
            return
        else:
            return error(alumno, alumnosBDD)
    
    def actualizarProfesorAlumno(self, alumno, profesor, curso, division, alumnosBDD):
        print(f"\nSe ha modificado el profesor de cursada correctamente.")
        alumno.profesor = profesor
        alumno.curso = curso
        alumno.division = division
        alumnosBDD.actualizarArchivo()
        return

    def modificarProfesorAlumno(self, alumno, profesoresBDD):
        def error(*args):
            while True:
                print("Seleccione una opcion: ")
                print("[1] Intentar Nuevamente")
                print("[0] Volver")
                opcion = input("Opcion: ")
                if opcion == "1":
                    return self.modificarProfesorAlumno(*args)
                elif opcion == "0":
                    return None
                else:
                    print("Ingrese una opcion valida.\n")

        materia = alumno.materia

        inputProfesor = input("\n1. Ingrese el profesor: ")
        validarProfesor = profesoresBDD.validarProfesorAlumno(materia, inputProfesor)

        if validarProfesor:
            print("Profesor registrado.")
            return inputProfesor
        else:
            return error(alumno, profesoresBDD)

    def modificarCursoAlumno(self, alumno, profesor, profesoresBDD):
        def error(*args):
            while True:
                print("Seleccione una opcion: ")
                print("[1] Intentar Nuevamente")
                print("[0] Volver")
                opcion = input("Opcion: ")
                if opcion == "1":
                    return self.modificarCursoAlumno(*args)
                elif opcion == "0":
                    return None
                else:
                    print("Ingrese una opcion valida.\n")

        materia = alumno.materia

        inputCurso = input("\n2. Ingrese el curso: ")
        validarCurso = profesoresBDD.validarCursoAlumno(materia, profesor, inputCurso)

        if validarCurso:
            print("Curso registrado.")
            return inputCurso
        else:
            return error(alumno, profesor, profesoresBDD)

    def modificarDivisionAlumno(self, alumno, profesor, curso, profesoresBDD):
        def error(*args):
            while True:
                print("Seleccione una opcion: ")
                print("[1] Intentar Nuevamente")
                print("[0] Volver")
                opcion = input("Opcion: ")
                if opcion == "1":
                    return self.modificarDivisionAlumno(*args)
                elif opcion == "0":
                    return None
                else:
                    print("Ingrese una opcion valida.\n")

        materia = alumno.materia

        inputDivision = input("\n3. Ingrese la division: ")
        validarDivision = profesoresBDD.validarDivisionAlumno(materia, profesor, curso, inputDivision)

        if validarDivision:
            print("Division registrada.")
            return inputDivision
        else:
            return error(alumno, profesor, curso, profesoresBDD)

    def modificarFecha(self, alumno, alumnosBDD):
        def error(*args):
            while True:
                print("Seleccione una opcion: ")
                print("[1] Intentar Nuevamente")
                print("[0] Volver")
                opcion = input("Opcion: ")
                if opcion == "1":
                    return self.modificarFecha(*args)
                elif opcion == "0":
                    return
                else:
                    print("Ingrese una opcion valida.\n")

        while True:
            inputFecha = input("\n1. Ingrese la nueva fecha de inscripcion en formato DD/MM/AA: ")
            try:
                dia, mes, anio = map(int, inputFecha.split("/"))
                if not (1 <= dia <= 31):
                    print("El dia ingresado esta fuera de un rango valido.\n")
                    raise
                if not (1 <= mes <= 12):
                    print("El mes ingresado esta fuera de un rango valido.\n")
                    raise
                if not (0 <= anio <= 99):
                    print("El año de inscripcion esta fuera de un rango valido.\n")
                    raise
                print(f"\nSe ha modificado la fecha correctamente a: {inputFecha}.")
                alumno.fecha = inputFecha
                alumnosBDD.actualizarArchivo()
                return
            except:
                print("El formato ingresado es invalido.\n")
                return error(alumno, alumnosBDD)
            