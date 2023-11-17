import TDA_Profesor as Profesor

def formatearArchivoInscripciones():
    diccionario = {}

    with open("Inscripciones.txt", "r") as archivo:
        listaInscriptos = [estudiante.strip() for estudiante in archivo]

        for estudiante in listaInscriptos:
            clavesDeEstudiantes = estudiante.split(",")
            fecha, nombre, materia, profesor, curso, division, nota = clavesDeEstudiantes
            diccionario[nombre] = [fecha, materia, profesor, curso, division, int(nota)]

    return diccionario

def actualizarArchivo():
    lineas = []

    for alumno, datos in inscripciones.items():
        duplicarDatos = datos.copy()
        duplicarDatos.insert(1, alumno)
        lineaFormateada = ",".join(str(dato) for dato in duplicarDatos) + "\n"
        lineas.append(lineaFormateada)

    with open("Inscripciones.txt", "w") as archivo:
        archivo.writelines(lineas)

inscripciones = formatearArchivoInscripciones()

profesores = Profesor.formatearArchivoProfesores()

#############################################
# opciones encargados
#############################################
# utilidades de funciones

def errorIntentarNuevamente(funcion, *args):
    while True:
        print("Seleccione una opcion: ")
        print("[1] Intentar Nuevamente")
        print("[0] Volver")
        opcion = input("Opcion: ")
        if opcion == "1":
            return funcion(*args)
        elif opcion == "0":
            return None
        else:
            print("Ingrese una opcion valida.\n")

def menuSeleccionarAlumno():
    print("\n----- Modificar Datos de Alumno -----")
    print("[1] Ver Alumnos")
    print("[2] Seleccionar Alumno")
    print("[0] Volver")
    opcion = input("Opcion: ")
    return opcion

def menuModificarDatos():
    print("\n----- Modificar Datos de Alumno -----")
    print("[1] Modificar Nombre")
    print("[2] Cambiar Profesor, Materia, Curso y Division")
    print("[3] Modificar Fecha de Inscripcion")
    print("[0] Volver")
    opcion = input("Opcion: ")
    return opcion

# funciones inscripciones

def verAlumnos():
    alumnos = ", ".join(inscripciones.keys())
    print("\nLista de alumnos: ")
    print(alumnos)

def validarAlumno():
    nombre = input("\n1. Ingrese el nombre del Alumno: ")
    if inscripciones.get(nombre, False):
        return nombre
    else:
        print(f"El alumno {nombre} no se encuentra en el sistema!\n")
        return errorIntentarNuevamente(validarAlumno)

def ingresarNombreEstudiante(textoInput):
    nombre = input(textoInput)
    if nombre not in inscripciones:
        print(f"Nombre registrado.")
        return nombre
    else:
        print("El alumno ya se encuentra inscripto en el sistema.\n")
        return errorIntentarNuevamente(ingresarNombreEstudiante, textoInput)

def ingresarFecha(textoInput):
    while True:
        fecha = input(textoInput)
        try:
            dia, mes, anio = map(int, fecha.split("/"))
            if not (1 <= dia <= 31):
                print("El dia ingresado esta fuera de un rango valido.\n")
                raise
            if not (1 <= mes <= 12):
                print("El mes ingresado esta fuera de un rango valido.\n")
                raise
            if not (0 <= anio <= 99):
                print("El año de inscripcion esta fuera de un rango valido.\n")
                raise
            print(f"Fecha ingresada: {fecha}.")
            return fecha
        except:
            print("El formato ingresado es invalido.\n")
            return errorIntentarNuevamente(ingresarFecha, textoInput)

def validarMateria(textoInput):
    materia = input(textoInput)
    for datosProfesor in profesores.values():
        if materia in datosProfesor:
            print("Materia registrada.")
            return materia
    else:
        print(f"La materia ingresada no esta disponible.\n")
        return errorIntentarNuevamente(validarMateria, textoInput)

def validarProfesor(materia, textoInput):
    profesor = input(textoInput)
    if profesor in profesores:
        if materia in profesores[profesor]:
            print("Profesor registrado.")
            return profesor
        else:
            print(f"El profesor ingresado no dicta la materia {materia}.\n")
            return errorIntentarNuevamente(validarProfesor, materia)
    else:
        print("El profesor ingresado no se encuentra en sistema.\n")
        return errorIntentarNuevamente(validarProfesor, materia, textoInput)

def validarCurso(profesor, materia, textoInput):
    profesorDatos = profesores[profesor]
    curso = input(textoInput)
    if curso in profesorDatos and materia in profesorDatos:
        print("Curso registrado.")
        return curso
    else:
        print(f"No existe ese curso para el profesor {profesor} en la materia {materia}.\n")
        return errorIntentarNuevamente(validarCurso, profesor, materia, textoInput)

def validarDivision(profesor, materia, curso, textoInput):
    profesorDatos = profesores[profesor]
    division = input(textoInput)
    if [materia, curso, division] == profesorDatos:
        print("Division registrada.")
        return division
    else:
        print(f"No existe la division ingresada para el profesor {profesor} en la materia {materia} del curso {curso}.\n")
        return errorIntentarNuevamente(validarDivision, profesor, materia, curso, textoInput)

# funciones modificar datos

def modificarNombreAlumno(nombre):
    inputText = "\n1. Ingrese el nuevo nombre del alumno: "
    alumno = ingresarNombreEstudiante(inputText)
    if alumno is None:
        return
    else:
        datosAlumno = inscripciones[nombre]
        inscripciones[alumno] = datosAlumno
        del inscripciones[nombre]
        actualizarArchivo()
        print(f"\nSe ha modificado el nombre correctamente a: {alumno}.")
        return alumno

def cambiarProfesor(nombre):
    materia = inscripciones[nombre][1]
    inputText = "\n1. Ingrese el nuevo profesor: "
    profesor = validarProfesor(materia, inputText)
    if profesor is None:
        return

    inputText = "\n2. Ingrese el curso: "
    curso = validarCurso(profesor, materia, inputText)
    if curso is None:
        return

    inputText = "\n3. Ingrese la division: "
    division = validarDivision(profesor, materia, curso, inputText)
    if division is None:
        return
    else:
        inscripciones[nombre][2] = profesor
        inscripciones[nombre][3] = curso
        inscripciones[nombre][4] = division
        actualizarArchivo()
        print(f"\nSe ha modificado el profesor asignado correctamente.")
        return

def modificarFecha(nombre):
    inputText = "\n1. Ingrese la nueva fecha de inscripcion en formato DD/MM/AA: "
    fecha = ingresarFecha(inputText)
    if fecha is None:
        return
    else:
        inscripciones[nombre][0] = fecha
        actualizarArchivo()
        print(f"\nSe ha modificado la fecha correctamente.")
        return

# opciones

def inscribirAlumno():
    inputText = "\n1. Ingrese el nombre completo del alumno: "
    nombre = ingresarNombreEstudiante(inputText)
    if nombre is None:
        return

    inputText = "\n2. Ingrese la fecha de inscripcion en formato DD/MM/AA: "
    fecha = ingresarFecha(inputText)
    if fecha is None:
        return

    inputText = "\n3. Ingrese la materia que va a cursar: "
    materia = validarMateria(inputText)
    if materia is None:
        return

    inputText = "\n4. Ingrese el profesor: "
    profesor = validarProfesor(materia, inputText)
    if profesor is None:
        return

    inputText = "\n5. Ingrese el curso: "
    curso = validarCurso(profesor, materia, inputText)
    if curso is None:
        return

    inputText = "\n6. Ingrese la division: "
    division = validarDivision(profesor, materia, curso, inputText)
    if division is None:
        return
    else:
        inscripciones[nombre] = [fecha, materia, profesor, curso, division, -1]
        actualizarArchivo()
        print(f"\nSe ha inscripto al alumno {nombre} a la materia {materia}.")
        return

def modificarInscripcion():
    while True:
        # menu ver o buscar alumno
        opcion = menuSeleccionarAlumno()

        if opcion == "1":
            verAlumnos()

        elif opcion == "2":
            alumno = validarAlumno()
            if alumno != None:

                while True:
                    # menu modificar datos
                    opcionModificarDatos = menuModificarDatos()

                    if opcionModificarDatos == "1":
                        alumno = modificarNombreAlumno(alumno)
                    elif opcionModificarDatos == "2":
                        cambiarProfesor(alumno)
                    elif opcionModificarDatos == "3":
                        modificarFecha(alumno)
                    elif opcionModificarDatos == "0":
                        break
                    else:
                        print("Ingrese una opcion valida.")

        elif opcion == "0":
            return

        else:
            print("Ingrese una opcion valida.")

def eliminarAlumno():
    alumno = validarAlumno()
    if alumno != None:
        del inscripciones[alumno]
        actualizarArchivo()
        print(f"Alumno {alumno} eliminado!")
        return
    else:
        return

#############################################
# opciones profesores
#############################################
# opciones

def verNota():
    alumno = validarAlumno()
    if alumno != None:
        nota = inscripciones[alumno][-1]
        print(f"Alumno: {alumno} - Calificacion: {nota}")
    else:
        return

def cargarNota():
    alumno = validarAlumno()
    if alumno != None:
        nota = inscripciones[alumno][-1]

        while True:
            if nota == -1:
                try:
                    nuevaNota = int(input("Ingrese la calificacion del Alumno: "))
                    if 0 <= nuevaNota <= 10:
                        inscripciones[alumno][-1] = nuevaNota
                        actualizarArchivo()
                        print("Nota cargada!")
                        return
                    else:
                        print("La nota ingresada no es valida! (0 a 10)\n")
                except:
                    print("La nota debe ser un valor numerico!\n")
            else:
                return print("La nota ya ha sido cargada! seleccione la opcion de modificar nota desde el menu.")
    else:
        return

def modificarNota():
    alumno = validarAlumno()
    if alumno != None:
        nota = inscripciones[alumno][-1]

        while True:
            if nota != -1:
                try:
                    nuevaNota = int(input("Ingrese la calificacion del Alumno: "))
                    if 0 <= nuevaNota <= 10:
                        inscripciones[alumno][-1] = nuevaNota
                        actualizarArchivo()
                        print("Nota modificada!")
                        return
                    else:
                        print("La nota ingresada no es valida! (0 a 10)\n")
                except:
                    print("La nota debe ser un valor numerico!\n")
            else:
                print("La nota aun no se ha cargado, por lo que no puede ser modificada.")
                return
    else:
        return

def eliminarNota():
    alumno = validarAlumno()
    if alumno != None:
        nota = inscripciones[alumno][-1]
        if nota != -1:
            inscripciones[alumno][-1] = -1
            actualizarArchivo()
            print("Se ha eliminado la nota del alumno.")
            return
        else:
            print("La nota ya se encontraba sin cargar.")
    else:
        return
