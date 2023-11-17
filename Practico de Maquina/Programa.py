import TDA_Encargado as Encargado
import TDA_Profesor as Profesor
import TDA_Inscripciones as Inscripciones

def menuPrincipal(num):
    if num == 1:
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

opcion = -1
inicializacion = 0

while opcion != "0":
    # menu principal
    opcion = menuPrincipal(inicializacion)
    inicializacion = 1

    if opcion == "1":  # opcion de encargados
        if Encargado.validarIngresoEncargado():

            while True:
                # menu de encargados
                opcionEncargado = menuEncargados()

                if opcionEncargado == "1":
                    Inscripciones.inscribirAlumno()
                elif opcionEncargado == "2":
                    Inscripciones.modificarInscripcion()
                elif opcionEncargado == "3":
                    Inscripciones.eliminarAlumno()
                elif opcionEncargado == "0":
                    break
                else:
                    print("Ingrese una opcion valida.")

    elif opcion == "2":  # opcion de profesores
        if Profesor.validarIngresoProfesor():

            while True:
                # menu de profesores
                opcionProfesor = menuProfesores()

                if opcionProfesor == "1":
                    Inscripciones.verNota()
                elif opcionProfesor == "2":
                    Inscripciones.cargarNota()
                elif opcionProfesor == "3":
                    Inscripciones.modificarNota()
                elif opcionProfesor == "4":
                    Inscripciones.eliminarNota()
                elif opcionProfesor == "0":
                    break
                else:
                    print("Ingrese una opcion valida.")

    elif opcion == "0":
        print("Programa finalizado.")

    else:
        print("Ingrese una opcion valida.")
