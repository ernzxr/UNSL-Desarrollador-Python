# //////// Ejercicio 1 ////////
print("\nEjercicio 1")

n = int(input("Ingrese un numero: "))

for num in range(n + 1):
    if num % 2 == 0:
        print(num)

# //////// Ejercicio 2 ////////
print("\nEjercicio 2")

n = int(input("Ingrese un numero: "))

suma = 0

for num in range(1, n+1):
    suma += num

print(f"La suma de los primeros {n} numeros naturales es {suma}.")

# //////// Ejercicio 3 ////////
print("\nEjercicio 3")

n = int(input("Ingrese un numero para saber su tabla de multiplos: "))

for num in range(10):
    print(f"{n} * {num} = {n * num}")

# //////// Ejercicio 4 ////////
print("\nEjercicio 4")

numeros = input("Ingrese dos numeros separados por espacios: ").split(" ")
n = int(numeros[0])
m = int(numeros[1])

bandera = 0

for num in range(0, m + 1):
    if n == 0:
        print("No se puede divir por 0.")
        break
    if num % n == 0:
        print(f"{num} es divisible por {n}.")

# //////// Ejercicio 5 ////////
print("\nEjercicio 5")

maximoYMinimo = []
maxChecker = minChecker = maximo = minimo = 0
i = 1

totalNumeros = int(input("Ingrese la cantidad de numeros que quiere cargar: "))

while i <= totalNumeros:
    n = int(input(f"{i}. Ingrese un numero: "))
    if maxChecker == 0:
        maximo = n
        maxChecker = 1
    elif minChecker == 0:
        if n > maximo:
            minimo = maximo
            maximo = n
            minChecker = 1
        else:
            minimo = n
            minChecker = 1
    elif n > maximo:
        maximo = n
    elif n < minimo:
        minimo = n
    i = i + 1

if totalNumeros > 1:
    maximoYMinimo.append(maximo)
    maximoYMinimo.append(minimo)
    print(f"El numero maximo es {maximoYMinimo[0]} y el minimo {maximoYMinimo[1]}")
elif totalNumeros == 1:
    print(f"Se ingreso un solo numero: {maximo}")
else:
    print("No se ingresaron numeros.")

# //////// Ejercicio 6 ////////
print("\nEjercicio 6")

contador = 0
n = int(input("Ingrese un numero o ingrese [-1] para cancelar la inicializacion del programa: "))

while n != -1:
    contador += 1
    n = int(input("Ingrese un numero o ingrese [-1] para salir del programa: "))

print("Se ingresaron", contador, "numeros.")

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

# //////// Ejercicio 8 ////////
print("\nEjercicio 8")

s = input("Ingrese un string: ").lower()
ultimoIndice = len(s) - 1
palindromo = 1
i = 0

while palindromo != None and i <= ultimoIndice:
    if s[i] != s[ultimoIndice - i]:
        palindromo = None
    i += 1

if palindromo:
    print(f"'{s}' es palindromo.")
else:
    print(f"'{s}' no es palindromo.")

# //////// Ejercicio 9 ////////
print("\nEjercicio 9")

s = input("Ingrese strings separados por espacio: ").split(" ")

maxStringLen = s[0]

for string in s:
    if len(string) > len(maxStringLen):
        maxStringLen = string

print(maxStringLen)

print(f"El string con mayor longitud es '{maxStringLen}'")

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

# //////// Ejercicio 13 ////////
print("\nEjercicio 13")

numeros = [int(num) for num in input("Ingrese numeros separados por espacios: ").split()]

negativos = positivos = neutro = 0

for num in numeros:
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        neutro += 1

if negativos == positivos:
    print(f"Hay {positivos} numeros positivos y negativos.")
elif negativos > positivos:
    print(f"Hay mas numeros negativos que positivos: {negativos} negativos y {positivos} positivos")
else:
    print(f"Hay mas numeros positivos que negativos: {positivos} positivos y {negativos} negativos")

if neutro > 0:
    print(f"Hay {neutro} de ceros.")
else:
    print("No hay ceros en la lista de numeros.")

# //////// Ejercicio 14 ////////
print("\nEjercicio 14")

elementos = input("Ingrese strings y/o numeros separados por espacios: ").split()

for i in range(len(elementos)):
    if elementos[i].isdigit():
        elementos[i] = int(elementos[i])

numerosCount = 0
stringsCount = 0

for element in elementos:
    if isinstance(element, int):
        numerosCount = numerosCount + 1
    elif isinstance(element, str):
        stringsCount = stringsCount + 1

print(f"Hay {numerosCount} numeros en la lista y {stringsCount} strings en la lista.")

# //////// Ejercicio 15 ////////
print("\nEjercicio 15")

listaMercaderia = []
bandera = 1
numeroProducto = 1

while bandera != 0:
    mercaderia = input(f"{numeroProducto}. Ingrese el nombre del producto: ")
    precio = int(input(f"Ingrese el precio del producto '{mercaderia}': "))

    listaMercaderia.append(mercaderia)
    listaMercaderia.append(precio)
    numeroProducto = numeroProducto + 1

    bandera = int(input("Ingrese [0] para salir del programa o [1] para continuar: "))

listaMercaderiaTupla = tuple(listaMercaderia)

for num in range(0, len(listaMercaderiaTupla), 2):
    print(f"Producto: {listaMercaderiaTupla[num]} - Precio: {listaMercaderia[num + 1]}$")

# //////// Ejercicio 16 ////////
print("\nEjercicio 16")

notasAlumno = []
i = 1

n = int(input("Ingrese la cantidad de materias a cargar del alumno: "))

while i <= n:
    materiaNota = input(f"{i}. Ingrese la materia y nota obtenida separada por un espacio: ").split()
    materiaNota[1] = int(materiaNota[1])
    notasAlumno.append(tuple(materiaNota))
    i += 1

totalMaterias = len(notasAlumno)
acumuladorNotas = 0

for nota in notasAlumno:
    acumuladorNotas += nota[1]

if totalMaterias > 0:
    promedio = acumuladorNotas / totalMaterias
    print(f"El promedio del alumno es de {promedio}")
else:
    print("No se ingresaron materias.")

# //////// Ejercicio 17 ////////
print("\nEjercicio 17")

notasAlumnoTrimestral = {}

for num in range(1,4):
    notasAlumno = []
    i = 1
    n = int(input(f"Trimestre #{num}. Ingrese la cantidad de materias a cargar: "))
    while i <= n:
        materiaNota = input(f"{i}. Ingrese la materia y nota obtenida separada por un espacio: ").split()
        materiaNota[1] = int(materiaNota[1])
        notasAlumno.append(tuple(materiaNota))
        i += 1
    else:
        notasAlumnoTrimestral[num] = notasAlumno

totalMaterias = 0
acumuladorNotas = 0

for trimestre in notasAlumnoTrimestral.values():
    totalMaterias += len(trimestre)
    for nota in trimestre:
        acumuladorNotas += nota[1]

if totalMaterias > 0:
    promedio = acumuladorNotas / totalMaterias
    print(f"El promedio del alumno es de {promedio}")
else:
    print("No se ingresaron materias.")

# //////// Ejercicio 18 ////////
print("\nEjercicio 18")

diccionario = {}

n_elements = int(input("Ingrese la cantidad de elementos a agregar al diccionario: "))

for i in range (1, n_elements + 1):
    clave = input(f"{i}. Ingrese una clave de tipo string: ")
    valor = [int(num) for num in input("Ingrese una lista de numeros separados por espacios: ").split()]
    diccionario[clave] = valor

print(f"Diccionario: {diccionario}")

for key, value in diccionario.items():
    print(f"Clave {key} - Valores: ")
    for item in value:
        print(f"{item}")

# //////// Ejercicio 19 ////////
print("\nEjercicio 19")

diccionario_19 = {}

n_elements = int(input("Ingrese la cantidad de elementos a agregar al diccionario: "))

for i in range (1, n_elements + 1):
    clave = int(input(f"{i}. Ingrese una clave numerica: "))
    valor = input("Ingrese un string: ")
    diccionario_19[clave] = valor

max_string = ""
max_string_key = None

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