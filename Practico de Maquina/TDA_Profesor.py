def formatearArchivoProfesores():
    diccionario = {}

    with open("Profesores.txt", "r") as archivo:
        listaProfesores = [profesor.strip() for profesor in archivo]

        for profesor in listaProfesores:
            clavesDeProfesor = profesor.split(",")
            nombre, materia, curso, division = clavesDeProfesor
            diccionario[nombre] = [materia, curso, division]

    return diccionario

def validarIngresoProfesor():
    def error():
        while True:
            print("Seleccione una opcion: ")
            print("[1] Intentar nuevamente")
            print("[0] Volver")
            opcion = input("Opcion: ")
            if opcion == "1":
                return validarIngresoProfesor()
            elif opcion == "0":
                return False
            else:
                print("Ingrese una opcion valida.\n")

    try:
        nombre = input("\n1. Ingrese su nombre completo: ")
        datosProfesor = profesores[nombre]
    except:
        print("El nombre ingresado no existe!\n")
        return error()
    else:
        materia = input("2. Materia que dicta: ")
        curso = input("3. Curso: ")
        division = input("4. Division: ")
        if [materia, curso, division] == datosProfesor:
            print(f"Acceso concedido.")
            print(f"\nBienvenido {nombre}!.")
            return True
        else:
            print("Ingreso invalido!\n")
            return error()

profesores = formatearArchivoProfesores()