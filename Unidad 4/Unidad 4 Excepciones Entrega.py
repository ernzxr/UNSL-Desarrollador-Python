# //////// Ejercicio 4 ////////
print("\nEjercicio 4")

noError = False
while not noError:
    try:
        elementosDiccionario = int(input("Ingrese la cantidad de elementos que desea agregar al diccionario: "))
    except ValueError:
        print("Ingrese un valor numerico!\n")
    else:
        diccionario = {}
        for i in range(1, elementosDiccionario + 1):
            clave = input(f"{i}. Ingrese una clave: ")
            valor = input("Ingrese un valor: ")
            diccionario[clave] = valor
        noError = True

opcion = ""
while opcion != "s":
    print("Elija una opcion: ")
    try:
        opcion = input("Ver Diccionario [V] - Insertar [I] - Modificar [M] - Eliminar [E] - Salir [S]: ").lower()
        if opcion not in "vimes":
            raise ValueError
    except ValueError:
        print("Por favor elija una opcion valida!\n")
    else:
        if opcion == "i":
            print("Insertar elemento")
            try:
                clave = input(f"Ingrese una clave: ")
                claveRepetida = False
                for key in diccionario.keys():
                    if clave == key:
                        claveRepetida = True
                if claveRepetida:
                    raise KeyError
            except KeyError:
                print("La clave ya existe! desea modificarla?")
                exceptOption = input("S/N: ").lower()
                if exceptOption == "s":
                    valor = input("Ingrese un valor: ")
                    diccionario[clave] = valor
                    print("Elemento modificado.\n")
                else:
                    print("\n")
            else:
                valor = input("Ingrese un valor: ")
                diccionario[clave] = valor
                print("Elemento agregado.\n")
        elif opcion == "m":
            print("Modificar elemento")
            try:
                clave = input(f"Ingrese una clave valida para modificarla: ")
                if diccionario[clave]:
                    diccionario[clave] = input("Ingrese un nuevo valor: ")
            except KeyError:
                print("La clave ingresada no existe!\n")
            else:
                print("Elemento modificado!\n")
        elif opcion == "e":
            try:
                del diccionario[input(f"Ingrese una clave valida para eliminarla: ")]
            except KeyError:
                print("La clave ingresada no existe y por ende no puede ser eliminada!\n")
            else:
                print("Clave eliminada!\n")
        elif opcion == "v":
            print(diccionario, "\n")
        else:
            print("Fin del programa.")
