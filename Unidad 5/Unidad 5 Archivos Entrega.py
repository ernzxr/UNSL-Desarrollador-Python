# //////// Ejercicio 6 ////////
print("\nEjercicio 6")

nombreDeArchivo = input("Ingrese un nombre de archivo para abrirlo: ")

with open(nombreDeArchivo, "r") as archivo:
    archivoContenido = " ".join(archivo.readlines()).split()

    for num in range(len(archivoContenido)):
        palabra = archivoContenido[num]
        if not palabra.isalpha():
            palabraAlpha = "".join(caracter.lower() for caracter in palabra if caracter.isalpha())
            archivoContenido[num] = palabraAlpha
        else:
            archivoContenido[num] = palabra.lower()

    while "" in archivoContenido:
        archivoContenido.remove("")

    diccionario = {}

    if len(archivoContenido) > 0:
        for palabra in archivoContenido:
            if palabra not in diccionario.keys():
                diccionario[palabra] = 1
            else:
                diccionario[palabra] += 1

    if len(diccionario) >= 5:
        clavesOrdenadas = sorted(diccionario, key=diccionario.get, reverse=True)
        primerasCincoPalabras = clavesOrdenadas[:5]

        numerador = 1
        for palabra in primerasCincoPalabras:
            contador = diccionario[palabra]
            print(f'{numerador}. Palabra: "{palabra}" - Apariciones: {contador}')
            numerador += 1
    elif len(diccionario) > 0:
        print(diccionario)
    else:
        print("No hay palabras en el archivo.")

# //////// Ejercicio 9 ////////
print("\nEjercicio 9")
print("-----El formato del archivo deben ser numeros enteros y/o flotantes separados por coma (,) sin espacios.-----\n")

def numeroValido(numero):
    numeroFormateado = "".join(caracter for caracter in numero if caracter.isdigit() or caracter == ".")
    return float(numeroFormateado)

nombreDeArchivo2 = input("Ingrese un nombre de archivo para abrirlo: ")

acumulador = 0

with open(nombreDeArchivo2, "r") as archivo:
    for linea in archivo:
        numeros = linea.split(",")
        for numero in numeros:
            acumulador += numeroValido(numero)

    print(f"El resultado de la suma de los numeros es: {acumulador}")

# //////// Ejercicio 10 ////////
print("\nEjercicio 10")
print("-----El archivo de texto a abrir debe contener una linea vacia al final.-----\n")

nombreDeArchivo3 = input("Ingrese un nombre de archivo para abrirlo: ")

with open(nombreDeArchivo3, 'r') as archivo:
    lineas = archivo.readlines()
    lineas = lineas[::-1]

with open(nombreDeArchivo3, 'w') as archivo:
    archivo.writelines(lineas)
    print("El orden de las líneas ha sido invertido correctamente.")

# //////// Ejercicio 11 ////////
print("\nEjercicio 11")

nombreDeArchivo4 = input("Ingrese un nombre de archivo para abrirlo: ")

with open(nombreDeArchivo4, "r") as archivo:
    lineas = archivo.readlines()

    for linea in lineas:
        indiceLinea = lineas.index(linea)
        palabras = linea.split()
        palabrasInvertidas = [palabra[::-1] for palabra in palabras]
        lineas[indiceLinea] = " ".join(palabrasInvertidas) + "\n"

with open(nombreDeArchivo4, "w") as archivo:
    archivo.writelines(lineas)
    print("El archivo ha sido modificado exitosamente.")

# //////// Ejercicio 12 ////////
print("\nEjercicio 12")

nombreDeArchivo5 = input("Ingrese un nombre de archivo para abrirlo: ")

with open(nombreDeArchivo5, "r") as archivo:
    lineas = archivo.readlines()

    for i in range(len(lineas)):
        palabras = lineas[i].split()
        palabras_invertidas = [palabra[::-1] for palabra in palabras]
        lineas[i] = " ".join(palabras_invertidas) + "\n"

    lineas = lineas[::-1]

with open(nombreDeArchivo5, "w") as archivo:
    archivo.writelines(lineas)
    print("El archivo ha sido modificado exitosamente.")