from BDD_Profesores import BDD_Profesores
from BDD_Encargados import BDD_Encargados
from BDD_Alumnos import BDD_Alumnos

alumnosBDD = BDD_Alumnos()
encargadosBDD = BDD_Encargados()
profesoresBDD = BDD_Profesores()

alumnosBDD.formatearArchivo()
encargadosBDD.formatearArchivo()
profesoresBDD.formatearArchivo()

def menuPrincipal(inicializacion):
    if inicializacion == 1:
        print("\n----- Menu Principal -----")
    else:
        print("----- Menu Principal -----")
    print("[1] Ingreso Encargado")
    print("[2] Ingreso Profesor")
    print("[0] Salir")
    opcion = input("Opcion: ")
    return opcion

def menuEncargados():
    print("\n----- Menu Encargado -----")
    print("[1] Inscribir Alumno")
    print("[2] Modificar Inscripción")
    print("[3] Eliminar Alumno")
    print("[0] Volver")
    opcion = input("Opcion: ")
    return opcion

def menuProfesores():
    print("\n----- Menu Profesor -----")
    print("[1] Ver Nota de Alumno")
    print("[2] Cargar Nota")
    print("[3] Modificar Nota")
    print("[4] Eliminar Nota")
    print("[0] Volver")
    opcion = input("Opcion: ")
    return opcion

def inscripcionAlumno(encargado, alumnosBDD, profesoresBDD):
    nombre = encargado.ingresarNombreAlumno(alumnosBDD)
    if nombre is None:
        return

    fecha = encargado.ingresarFechaInscripcionAlumno()
    if fecha is None:
        return

    materia = encargado.ingresarMateriaAlumno(profesoresBDD)
    if materia is None:
        return

    profesor = encargado.ingresarProfesorAlumno(materia, profesoresBDD)
    if profesor is None:
        return

    curso = encargado.ingresarCursoAlumno(materia, profesor, profesoresBDD)
    if curso is None:
        return

    division = encargado.ingresarDivisionAlumno(materia, profesor, curso, profesoresBDD)
    if division is None:
        return

    return encargado.inscribirAlumno(nombre, fecha, materia, profesor, curso, division, alumnosBDD)

def modificarInscripcionProfesorAlumno(encargado, alumno, alumnosBDD, profesoresBDD):
    profesor = encargado.modificarProfesorAlumno(alumno, profesoresBDD)
    if profesor is None:
        return

    curso = encargado.modificarCursoAlumno(alumno, profesor, profesoresBDD)
    if curso is None:
        return

    division = encargado.modificarDivisionAlumno(alumno, profesor, curso, profesoresBDD)
    if division is None:
        return

    return encargado.actualizarProfesorAlumno(alumno, profesor, curso, division, alumnosBDD)

def modificarInscripcion(encargado, alumnosBDD):
    def menuSeleccionarAlumno():
        print("\n----- Seleccionar Alumno en Base de Datos -----")
        print("[1] Ver Alumnos")
        print("[2] Seleccionar Alumno")
        print("[0] Volver")
        opcion = input("Opcion: ")
        return opcion

    def menuModificarDatos():
        print("\n----- Modificar Datos de Alumno -----")
        print("[1] Modificar Nombre")
        print("[2] Cambiar Profesor, Curso y Division")
        print("[3] Modificar Fecha de Inscripcion")
        print("[0] Volver")
        opcion = input("Opcion: ")
        return opcion

    while True:
        # menu ver o buscar alumno
        opcion = menuSeleccionarAlumno()

        if opcion == "1":
            encargado.verAlumnos(alumnosBDD)

        elif opcion == "2":
            alumno = encargado.validarAlumno(alumnosBDD)
            if alumno:

                while True:
                    # menu modificar datos
                    opcionModificarDatos = menuModificarDatos()

                    if opcionModificarDatos == "1":
                        encargado.modificarNombreAlumno(alumno, alumnosBDD)
                    elif opcionModificarDatos == "2":
                        modificarInscripcionProfesorAlumno(encargado, alumno, alumnosBDD, profesoresBDD)
                    elif opcionModificarDatos == "3":
                        encargado.modificarFecha(alumno, alumnosBDD)
                    elif opcionModificarDatos == "0":
                        break
                    else:
                        print("Ingrese una opcion valida.")

        elif opcion == "0":
            return

        else:
            print("Ingrese una opcion valida.")

opcion = -1
inicializacion = 0

while opcion != "0":
    # menu principal
    opcion = menuPrincipal(inicializacion)
    inicializacion = 1

    if opcion == "1":  # opcion de encargados
        encargado = encargadosBDD.validarIngreso()
        if encargado:

            while True:
                # menu de encargados
                opcionEncargado = menuEncargados()

                if opcionEncargado == "1":
                    inscripcionAlumno(encargado, alumnosBDD, profesoresBDD)
                elif opcionEncargado == "2":
                    modificarInscripcion(encargado, alumnosBDD)
                elif opcionEncargado == "3":
                    encargado.eliminarAlumno(alumnosBDD)
                elif opcionEncargado == "0":
                    break
                else:
                    print("Ingrese una opcion valida.")

    elif opcion == "2":  # opcion de profesores
        profesor = profesoresBDD.validarIngreso()
        if profesor:

            while True:
                # menu de profesores
                opcionProfesor = menuProfesores()

                if opcionProfesor == "1":
                    profesor.verNota(alumnosBDD)
                elif opcionProfesor == "2":
                    profesor.cargarNota(alumnosBDD)
                elif opcionProfesor == "3":
                    profesor.modificarNota(alumnosBDD)
                elif opcionProfesor == "4":
                    profesor.eliminarNota(alumnosBDD)
                elif opcionProfesor == "0":
                    break
                else:
                    print("Ingrese una opcion valida.")

    elif opcion == "0":
        print("Programa finalizado.")

    else:
        print("Ingrese una opcion valida.")
