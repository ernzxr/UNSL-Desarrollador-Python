# //////// Ejercicio 2 ////////
print("\nEjercicio 2")

def listaNumerosEnteros():
    try:
        lista = [int(num) for num in input('Ingrese numeros separados por coma (","): ').split(",")]
    except:
        return []
    else:
        return lista

def pares(lista):
    listaPares = [num for num in lista if num % 2 == 0]
    return listaPares

def impares(lista):
    listaImpares = [num for num in lista if num % 2 != 0]
    return listaImpares

def mayoria(lista1, lista2):
    try:
        if lista1[0] % 2 == 0:
            par = lista1
            impar = lista2
        else:
            par = lista2
            impar = lista1
    except:
        print("Una de las listas esta vacia!")
    else:
        if len(par) > len(impar):
            print("Hay mayoria de numeros pares.")
        elif len(impar) > len(par):
            print("Hay mayoria de numeros impares.")
        else:
            print("Hay igual cantidad de numeros pares e impares.")

listaEnteros = listaNumerosEnteros()

listaDePares = pares(listaEnteros)
listaDeImpares = impares(listaEnteros)

mayoria(listaDeImpares, listaDePares)

# //////// Ejercicio 3 ////////
print("\nEjercicio 3")

def listaDeStrings():
    lista = input('Ingrese strings separados por coma (","): ').split(",")
    return lista

def crearDiccionarioClaveYContador(lista):
    diccionario = {}
    for palabra in lista:
        for letra in palabra:
            if letra.isalpha():
                if letra not in diccionario.keys():
                    diccionario[letra] = 1
                else:
                    diccionario[letra] += 1
    return diccionario

listaStrings = listaDeStrings()
print(crearDiccionarioClaveYContador(listaStrings))

# //////// Ejercicio 4 ////////
print("\nEjercicio 4")

def invertirString(stringValue):
    return stringValue[::-1]

listaStrings2 = listaDeStrings()

def invertirTodo(list):
    invertedList = []
    for palabra in list:
        invertedList.append(invertirString(palabra))
    return invertedList

listaStringsInvertida = invertirTodo(listaStrings2)

print(listaStrings2)
print(listaStringsInvertida)

# //////// Ejercicio 6 ////////
print("\nEjercicio 6")

def coordenadaZ(x, y):
    x = x + 10
    y = y + 15
    return x + y

x = int(input("Coordenada eje x: "))
y = int(input("Coordenada eje y: "))

for i in range(3):
    z = coordenadaZ(x, y)
    x = x + 1
    y = y + 1
    print (x, ".", y, ".", z)

coordenadaZ(x, y)

print('''\nEl programa se encarga de ejecutar un ciclo for 3 veces en donde previamente al ciclo se nos pide
que ingresemos el valor de las variables "x" y "y".
En el ciclo for, primeramente se asigna un valor numerico a la variable "z" con la utilizacion de una funcion, funcion que
se encarga de operar dos valores numericos, en este caso "x" y "y", y de devolver un resultado numerico.
Ademas, en cada ciclo, luego de utilizar los valores inicialmente ingresados para "x" y "y", se modifican los valores de "x"
y "y" para la proxima vuelta del ciclo.
Finalmente el programa imprime los valores de "x", "y" y "z" en cada vuelta del ciclo.
''')

# //////// Ejercicio 9 ////////
print("Ejercicio 9")

def agregarPersona(diccionario):
    dni = input("Ingrese DNI sin puntos: ")
    if validacionDNI(dni):
        nombre = input("Ingrese Nombre/s y Apellido: ")
        domicilio = input("Ingrese el Domicilio: ")
        diccionario[dni] = [nombre, domicilio, dni]
        print("Persona agregada al padron!")
        print(diccionario[dni])
    else:
        print("DNI Invalido.")

def removerPersona(diccionario, dni):
    try:
        del diccionario[dni]
    except KeyError:
        print("La persona ingresada no existe!")
    else:
        print("Persona removida del padron!")

def modificarDomicilio(diccionario, dni):
    try:
        diccionario[dni]
    except KeyError:
        print("La persona ingresada no existe!")
    else:
        domicilio = input("Ingrese el nuevo domicilio: ")
        diccionario[dni][1] = domicilio
        print("Domicilio modificado!")

def modificarNombre(diccionario, dni):
    try:
        diccionario[dni]
    except KeyError:
        print("La persona ingresada no existe!")
    else:
        nombre = input("Ingrese el nuevo Nombre/s y Apellido: ")
        diccionario[dni][0] = nombre
        print("Nombre modificado!")

def modificarDNI(diccionario, dni):
    try:
        datos = diccionario[dni]
    except KeyError:
        print("La persona ingresada no existe!")
    else:
        removerPersona(diccionario, dni)
        nuevoDNI = input("Ingrese el nuevo DNI: ")
        diccionario[nuevoDNI] = datos
        print("DNI modificado!")

def verPadron(diccionario):
    for persona in diccionario.values():
        print(persona)

def verDatosPersona(diccionario, dni):
    try:
        print(diccionario[dni])
    except KeyError:
        print("La persona ingresada no existe!")

def menuPrincipal():
    print("\nPadron - Opciones:")
    print("[1] Incorporar personas al padron.")
    print("[2] Remover personas del padron.")
    print("[3] Modificar datos de una persona.")
    print("[4] Buscar datos de una persona.")
    print("[5] Ver padron.")
    print("[0] Salir.")

def menuModificaciones():
    print("\nModificar datos - Opciones:")
    print("[1] Cambiar Nombre.")
    print("[2] Cambiar Domicilio.")
    print("[3] Cambiar DNI.")
    print("[0] Volver.")

padron = {}

opcion = -1
while opcion != 0:
    menuPrincipal()
    try:
        opcion = int(input("Ingrese una opcion: "))
        if opcion not in [0, 1, 2, 3, 4, 5]:
            raise ValueError
    except ValueError:
        print("Ingrese una opcion valida.")
    else:
        if opcion == 1:
            agregarPersona(padron)
        elif opcion == 2:
            dni = input("Ingrese DNI: ")
            if validacionDNI(dni):
                removerPersona(padron, dni)
            else:
                print("DNI Invalido.")
        elif opcion == 3:
            menuModificaciones()
            try:
                opcionModificacion = int(input("Ingrese una opcion: "))
                if opcionModificacion not in [0, 1, 2, 3]:
                    raise ValueError
            except ValueError:
                print("Opcion invalida, volviendo al menu anterior.")
            else:
                if opcionModificacion == 1:
                    dni = input("Ingrese DNI: ")
                    if validacionDNI(dni):
                        modificarNombre(padron, dni)
                    else:
                        print("DNI Invalido.")
                if opcionModificacion == 2:
                    dni = input("Ingrese DNI: ")
                    if validacionDNI(dni):
                        modificarDomicilio(padron, dni)
                    else:
                        print("DNI Invalido.")
                if opcionModificacion == 3:
                    dni = input("Ingrese DNI: ")
                    if validacionDNI(dni):
                        modificarDNI(padron, dni)
                    else:
                        print("DNI Invalido.")
        elif opcion == 4:
            dni = input("Ingrese DNI: ")
            if validacionDNI(dni):
                verDatosPersona(padron, dni)
            else:
                print("DNI Invalido.")
        elif opcion == 5:
            verPadron(padron)
        else:
            print("Programa finalizado!")