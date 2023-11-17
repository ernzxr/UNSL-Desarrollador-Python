def listaNumerosEnteros():
    try:
        lista = [int(num) for num in input('Ingrese numeros separados por coma (","): ').split(",")]
    except:
        return []
    else:
        return lista

# //////// Ejercicio 1 ////////
print("\nEjercicio 1")

def sumarPar(lista):
    acumulador = 0
    for num in lista:
        if num % 2 == 0:
            acumulador += num
    return acumulador

listaEnteros = listaNumerosEnteros()

print(sumarPar(listaEnteros))

# //////// Ejercicio 2 ////////
print("\nEjercicio 2")

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

listaEnteros2 = listaNumerosEnteros()

listaDePares = pares(listaEnteros2)
listaDeImpares = impares(listaEnteros2)

mayoria(listaDeImpares, listaDePares)

# //////// Ejercicio 3 ////////
print("\nEjercicio 3")

def listaDeStrings():
    lista = input('Ingrese strings separados por coma (","): ').split(",")
    return lista

def crearDiccionarioClaveLetraYContadorDeLetra(lista):
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
print(crearDiccionarioClaveLetraYContadorDeLetra(listaStrings))

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

# //////// Ejercicio 5 ////////
print("\nEjercicio 5")

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def menuCalculadora():
    print("[1] (+) | [2] (-) | [3] (*) | [4] (/) | [-1] Salir.")

print("\n+- Calculadora */\n")

primerCalculo = 0
resultado = 0
opcion = 1
while opcion != -1:
    if opcion in [1, 2, 3, 4]:
        if primerCalculo == 0:
            numero1 = int(input("Ingrese un numero: "))
            menuCalculadora()
            opcion = int(input("Elija una opcion: "))
            if opcion == -1:
                print("Gracias por utilizar la calculadora!")
                break
            numero2 = int(input("Ingrese otro numero: "))
        else:
            menuCalculadora()
            opcion = int(input("Elija una opcion: "))
            if opcion in [1, 2, 3, 4]:
                numero1 = int(input("Ingrese un numero: "))

    if opcion == 1:
        if primerCalculo == 0:
            resultado = suma(numero1, numero2)
            primerCalculo = 1
            print(resultado, "\n")
        else:
            resultado = suma(resultado, numero1)
            print(resultado, "\n")
    elif opcion == 2:
        if primerCalculo == 0:
            resultado = resta(numero1, numero2)
            primerCalculo = 1
            print(resultado, "\n")
        else:
            resultado = resta(resultado, numero1)
            print(resultado, "\n")
    elif opcion == 3:
        if primerCalculo == 0:
            resultado = multiplicacion(numero1, numero2)
            primerCalculo = 1
            print(resultado, "\n")
        else:
            resultado = multiplicacion(resultado, numero1)
            print(resultado, "\n")
    elif opcion == 4:
        if primerCalculo == 0:
            resultado = division(numero1, numero2)
            primerCalculo = 1
            print(resultado, "\n")
        else:
            resultado = division(resultado, numero1)
            print(resultado, "\n")
    elif opcion == -1:
        print("Gracias por utilizar la calculadora!")
    else:
        print("Ingrese una opcion valida.")

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

print('''El programa incrementa el valor de las variables 'x' y 'y' en 10 y 15 
para luego devolver el valor de la suma entre ambas variables.
Como resultado obtenemos el valor de la variable 'z' en tres puntos 
distintos que se operan a traves de un ciclo for.''')

# //////// Ejercicio 7 ////////
print("\nEjercicio 7")

def maximo(x, y):
    return x if x > y else y

def minimo(x, y):
    return x if x < y else y

x = int(input("Un numero: "))
y = int(input("Otro numero: "))

print(maximo(x - 3, minimo(x + 2, y - 5)))

print('''El programa tiene dos funciones que sirven para calcular el maximo y minimo entre dos numeros.
Se podrian agregar excepciones y validaciones por si se ingresan valores que no sean enteros para evitar errores.''')

# //////// Ejercicio 8 ////////
print("\nEjercicio 8")

dni = input("Ingrese un DNI: ")

def validacionDNI(value):
    try:
        dni = int(value)
        dniStr = str(dni)
        if not 6 < len(dniStr) < 9:
            raise
    except:
        return False
    else:
        return True

print(validacionDNI(dni))

# //////// Ejercicio 9 ////////
print("\nEjercicio 9")

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

# //////// Ejercicio 10 ////////
print("\nEjercicio 10")

def operandoConcatenando(value1, value2):
    try:
        return value1 + value2
    except:
        print("Los tipos de datos ingresados son distintos entre si.")

# //////// Ejercicio 11 ////////
print("\nEjercicio 11")

def listaNumerosFlotantes():
    try:
        lista = [float(num) for num in input('Ingrese numeros flotantes separados por coma (","): ').split(",")]
    except:
        return []
    else:
        return lista

def porcentaje(num, lista = []):
    acumulador = 0
    try:
        for number in lista:
            acumulador += number
    except:
        print("La lista esta vacia.")
    else:
        if acumulador != 0:
            return (100 * num) / acumulador, acumulador
        else:
            print("No se puede dividir por 0.")

listaDeFlotantes = listaNumerosFlotantes()

p = None
while p == None:
    try:
        p = int(input("Ingrese un numero entero: "))
    except:
        print("Ingrese un valor valido.\n")

try:
    porcentajeCalculado, acumulador = porcentaje(p, listaDeFlotantes)
except:
    pass
else:
    porcentajeCalculado = round(porcentajeCalculado, 2)
    print(f"El porcentaje de {p} en {acumulador} es {porcentajeCalculado}%")

# //////// Ejercicio 12 ////////
print("\nEjercicio 12")

def factorial(n):
    if n < 0:
        raise print("No se puede calcular el factorial en numeros negativos.")
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        raise print("No se aplican los numeros negativos a la serie de Fibonacci.")
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def potencia(n, m):
        return n ** m

try:
    n = int(input("Ingrese un número entero para calcular el factorial: "))
    print(f"El factorial de {n} es {factorial(n)}")
except:
    print("El valor ingresado no es valido.")

try:
    n = int(input("Ingrese un número entero para calcular el término de Fibonacci: "))
    print(f"El término {n} de la serie de Fibonacci es {fibonacci(n)}")
except:
    print("El valor ingresado no es valido.")

try:
    n = float(input("Ingrese la base de la potencia (n): "))
    m = int(input("Ingrese el exponente de la potencia (m): "))
    print(f"{n} elevado a la potencia {m} es igual a {potencia(n, m)}")
except:
    print("El valor ingresado no es valido.")