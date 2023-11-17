def formatearArchivoEncargados():
    diccionario = {}

    with open("Encargados.txt", "r") as archivo:
        listaEncargados = [encargado.strip() for encargado in archivo]

        for encargado in listaEncargados:
            clavesDeEncargado = encargado.split(",")
            nombre, dni = clavesDeEncargado
            diccionario[dni] = nombre

    return diccionario

def validarIngresoEncargado():
    def error():
        while True:
            print("Seleccione una opcion: ")
            print("[1] Intentar nuevamente")
            print("[0] Volver")
            opcion = input("Opcion: ")
            if opcion == "1":
                return validarIngresoEncargado()
            elif opcion == "0":
                return False
            else:
                print("Ingrese una opcion valida.\n")

    try:
        dni = input("\n1. Ingrese su DNI sin puntos: ")
        datosEncargado = encargados[dni]
    except:
        print("El DNI ingresado no existe!\n")
        return error()
    else:
        nombre = input("2. Ingrese su nombre completo: ")
        if nombre == datosEncargado:
            print(f"Acceso concedido.")
            print(f"\nBienvenido {nombre}!.")
            return True
        else:
            print("Ingreso invalido!\n")
            return error()

encargados = formatearArchivoEncargados()