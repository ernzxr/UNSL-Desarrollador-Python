# //////// Ejercicio 7 ////////
print("\nEjercicio 7")

consonante = 0
vocal = 0

s = input("Ingrese un string: ")

for letra in s:
    if letra in "aeiou":
        vocal += 1
    elif letra.isalpha():
        consonante += 1

if consonante > 0 and vocal > 0:
    print(f"El string '{s}' tiene {consonante} consonantes y {vocal} vocales.")
elif consonante > 0 and vocal == 0:
    print(f"El string '{s}' tiene {consonante} consonantes y 0 vocales.")
elif consonante == 0 and vocal > 0:
    print(f"El string '{s}' tiene 0 consonantes y {vocal} vocales.")

# //////// Ejercicio 9 ////////
print("\nEjercicio 9")

s = input("Ingrese strings separados por espacio: ").split(" ")

maxStringLen = len(s[0])
maxString = s[0]

for string in s:
    if len(string) > maxStringLen:
        maxStringLen = len(string)
        maxString = string

print(f"El string con mayor longitud es '{maxString}'")

# //////// Ejercicio 10 ////////
print("\nEjercicio 10")

s0 = input("Ingrese un string: ")
s1 = input("Ingrese otro string: ")

s0Len = len(s0)
s1Len = len(s1)

maxLen = max(s0Len, s1Len)

merge = ""

for num in range(maxLen):
    if num < s0Len:
        merge += s0[num]
    if num < s1Len:
        merge += s1[num]

print("s0:", s0)
print("s1:", s1)
print("merge:", merge)

# //////// Ejercicio 11 ////////
print("\nEjercicio 11")

l = input("Ingrese strings separados por espacio: ").split()

vocalesList = []
consonantesList = []

for palabra in l:
    for letra in palabra:
        if letra.lower() in "aeiou":
            vocalesList.append(letra.lower())
        elif letra.isalpha():
            consonantesList.append(letra.lower())

print("l:", l)
print("Vocales:", vocalesList)
print("Consonantes:", consonantesList)
print(f"Cantidad de vocales: {len(vocalesList)}")
print(f"Cantidad de consonantes: {len(consonantesList)}")

# //////// Ejercicio 12 ////////
print("\nEjercicio 12")

listaDeStrings = input("Ingrese strings separados por espacios: ").split()

print("Lista", listaDeStrings)

for i in range(len(listaDeStrings)):
    listaDeStrings[i] = listaDeStrings[i][::-1]

print("Lista invertida:", listaDeStrings)

# //////// Ejercicio 19 ////////
print("\nEjercicio 19")

diccionario_19 = {}

n_elements = int(input("Ingrese la cantidad de elementos a agregar al diccionario: "))

for i in range (1, n_elements + 1):
    clave = int(input(f"{i}. Ingrese una clave numerica: "))
    valor = input("Ingrese un string: ")
    diccionario_19[clave] = valor

max_string = ""

for key, value in diccionario_19.items():
    if len(value) > len(max_string):
        max_string = value
        max_string_key = key

print(f"Diccionario: {diccionario_19}")
print(f"La clave: '{max_string_key}' es la que contiene el string mas largo: '{max_string}'.")

# //////// Ejercicio 20 ////////
print("\nEjercicio 20")

cantidad_registros = int(input("Ingrese la cantidad de personas que va a cargar: "))

registros = []

for i in range(1, cantidad_registros + 1):
    persona = {}
    print(f"Datos #{i}:")
    dni = int(input("Ingrese DNI: "))
    nombre = input("Ingrese Nombre Completo: ")
    edad = int(input("Ingrese Edad: "))
    domicilio = input("Ingrese Domicilio: ")
    trabajos = tuple(input("Ingrese Trabajos separados por coma: ").split(","))
    persona[dni] = (nombre, edad, domicilio, trabajos)
    registros.append(persona)

busqueda = int(input("Ingrese un DNI para buscar sus datos: "))
encontrado = False

for persona in registros:
    if busqueda in persona.keys():
        encontrado = True
        print(f'DNI: {busqueda}\n'
        f'Nombre: {persona[busqueda][0]}\n'
        f'Edad: {persona[busqueda][1]}\n'
        f'Domicilio: {persona[busqueda][2]}')

        if len(persona[busqueda][3]) == 1:
            print(f'Trabajo: {persona[busqueda][3][0]}')
        else:
            trabajos_string = ", ".join(persona[busqueda][3][:-1]) + " y " + persona[busqueda][3][-1]
            print(f"Trabajos: {trabajos_string}")

if not encontrado:
    print("El DNI ingresado no se encuentra en la base de datos.")