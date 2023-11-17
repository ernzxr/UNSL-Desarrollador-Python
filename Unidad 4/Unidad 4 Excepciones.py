# //////// Ejercicio 1 ////////
print("\nEjercicio 1")

try:
    stringANumero = int(input("Ingrese un string: "))
except ValueError as err:
    print("Error de ingreso:", err)
else:
    print(stringANumero)

# //////// Ejercicio 2 ////////
print("\nEjercicio 2")

lista = []

noError = False
while not noError:
    try:
        totalElementosAgregar = int(input("Ingrese la cantidad de elementos a agregar: "))
        if totalElementosAgregar < 1:
            raise ValueError
    except ValueError:
        print("Dato invalido, debe ser un valor numerico mayor que 0.")
    else:
        for i in range(1, totalElementosAgregar + 1):
            elemento = input(f"{i}. Ingrese el elemento: ")
            lista.append(elemento)
        noError = True
    finally:
        print(f"Lista generada: {lista}")

noError = False
while not noError:
    print(f"Elija un numero en el rango de entre 0 y {len(lista) - 1} para modificar en la lista.")
    try:
        indice = int(input("Ingrese el indice: "))
        if indice < 0 or indice >= len(lista):
            raise IndexError
    except (ValueError, IndexError):
        print("Error: índice inválido. Asegúrese de ingresar un valor numérico dentro del rango válido.")
    else:
        elementoACargar = input(f"Ingrese el valor con el que desea modificar al indice {indice}: ")
        lista[indice] = elementoACargar
        noError = True
    finally:
        print(f"Lista actualizada: {lista}")

noError = False
while not noError:
    try:
        eliminarIndice = int(input("Ingrese un indice para eliminarlo de la lista: "))
        if eliminarIndice < 0 or eliminarIndice >= len(lista):
            raise IndexError
    except ValueError:
        print("Dato invalido, debe ser un valor numerico.")
    except IndexError:
        print(f"Indice fuera de rango, los indices validos estan entre 0 y {len(lista)}.")
    else:
        del lista[eliminarIndice]
        noError = True
    finally:
        print(f"Lista final: {lista}")

# //////// Ejercicio 3 ////////
print("\nEjercicio 3")

listaElementos = input("Ingrese los elementos de la lista separados por espacios: ").split()

noNumericos = []
sumaNumericos = 0

for i in listaElementos:
    try:
        i = float(i)
    except ValueError:
        noNumericos.append(i)
    else:
        sumaNumericos += i

print(f"La suma de los número es {sumaNumericos}")
print(f"La lista de los elementos no numéricos es {noNumericos}")

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
                diccionario[clave]
            except KeyError:
                print("La clave ingresada no existe!\n")
            else:
                diccionario[clave] = input("Ingrese un nuevo valor: ")
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
