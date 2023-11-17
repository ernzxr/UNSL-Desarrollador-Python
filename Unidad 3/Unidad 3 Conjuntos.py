# //////// Ejercicio 1 ////////
print("\nEjercicio 1")

provincias = {"Buenos Aires", "Catamarca", "Chaco", "Chubut", "Cordoba", "Corrientes", "Entre Rios", "Formosa", "Jujuy",
              "La Pampa", "La Rioja", "Mendoza", "Misiones", "Neuquen", "Rio Negro", "Salta", "San Juan", "San Luis",
              "Santa Cruz", "Santa Fe", "Santiago del Estero", "Tierra del Fuego", "Tucuman"}

provinciaIngresada = {input("Ingrese una provincia: ")}

complementoProvincias = provincias - provinciaIngresada

print(f"Provincias: {provincias}")
print(f"Provincia ingresada: {provinciaIngresada}")
print(f"Complemento entre conjuntos de provincias: {complementoProvincias}")

# //////// Ejercicio 2 ////////
print("\nEjercicio 2")

conjuntoUniversal = set(range(1, 21))

elementosConjuntoA = input("Ingrese los numeros del conjunto A separados por ',': ").split(",")
conjuntoArrayA = []

for elemento in elementosConjuntoA:
    conjuntoArrayA.append(int(elemento))

conjuntoA = set(conjuntoArrayA)

elementosConjuntoB = input("Ingrese los numeros del conjunto B separados por ',': ").split(",")
conjuntoB = set(int(num) for num in elementosConjuntoB)

union = conjuntoA | conjuntoB
interseccion = conjuntoA & conjuntoB
diferencia = union - interseccion

print(f"Conjunto A: {conjuntoA}")
print(f"Conjunto B: {conjuntoB}")
print(f"Union del Conjunto A y B: {union}")
print(f"Interseccion del Conjunto A y B: {interseccion}")
print(f"Complemento entre la union e interseccion del conjunto A y B: {diferencia}")

# //////// Ejercicio 3 ////////
print("\nEjercicio 3")

conjunto = {"a", "b", "c", "d"}
diccionarioValores = {}
diccionarioClaves = {}
diccionarioValor = {}

i = 1

for element in conjunto:
    diccionarioValores[i] = element
    diccionarioClaves[element] = i
    i += 1

diccionarioValor[1] = conjunto

print(f"Conjunto: {conjunto}")
print(f"1. Diccionario con un conjunto iterado en valores: {diccionarioValores}")
print(f"Diccionario con un conjunto iterado en claves: {diccionarioClaves}")
print(f"Diccionario con un conjunto como valor: {diccionarioValor}\n")

print('''2. No es posible pasar un set como elemento a un frozenset ya que un frozenset es inmutable.
Si se quiere transformar un set en frozenset basta con utilizar "frozenset(set())".\n''')

nuevoArray = ["e", "f"]
print(f"3. Array: {nuevoArray}")

nuevoArray.append(conjunto)
print(f"Array con un conjunto: {nuevoArray}")

nuevoArray = ["e", "f"]

for element in conjunto:
    nuevoArray.append(element)

print(f"Array con un conjunto iterado: {nuevoArray}\n")

ordenarConjunto = sorted(list(conjunto))

print(f'''4. No es posible ordenar un conjunto, ya que el mismo no puede ser ordenado, 
si se quiere ordenar se debe transformar a un tipo de dato que permita esta propiedad, como por ejemplo un lista:
{ordenarConjunto}\n''')

tuplaDeConjunto = tuple(conjunto)
tuplaConjuntoNoIterado = (conjunto,)

print(f'''5. Tupla de conjunto: {tuplaDeConjunto}
Tupla de conjunto sin iterar: {tuplaConjuntoNoIterado}''')

# //////// Ejercicio 4 ////////
print("\nEjercicio 4")

conjuntoUnoElementos = input("Ingrese numeros separados por ',' para el conjunto 1: ").split(",")
conjuntoUno = set(int(num) for num in conjuntoUnoElementos)

conjuntoDosElementos = input("Ingrese numeros separados por ',' para el conjunto 2: ").split(",")
conjuntoDos = set(int(num) for num in conjuntoDosElementos)

conjuntoUniversal = conjuntoUno | conjuntoDos

print(f"Conjunto 1: {conjuntoUno}")
print(f"Conjunto 2: {conjuntoDos}")
print(f"Conjunto Universal: {conjuntoUniversal}")

# //////// Ejercicio 5 ////////
print("\nEjercicio 5")

conjuntoA5Elementos = input("Ingrese numeros separados por ',' para el conjunto: ").split(",")
conjuntoA5 = set(int(num) for num in conjuntoA5Elementos)

cardinalidad = len(conjuntoA5)
maximoConjunto = max(conjuntoA5)
minimoConjunto = min(conjuntoA5)

print(f"Cardinalidad del conjunto: {cardinalidad}")
print(f"Maximo del conjunto: {maximoConjunto}")
print(f"Minimo del conjunto: {minimoConjunto}")

# //////// Ejercicio 6 ////////
print("\nEjercicio 6")

conjunto6Elementos = set(input("Ingrese valores separados por ',' para el conjunto: ").split(","))

valor6 = input("Ingrese un valor para buscarlo en el conjunto: ")

print(f"Conjunto: {conjunto6Elementos}")

if valor6 in conjunto6Elementos:
    print(f"El valor {valor6} se encontro en el conjunto.")
else:
    print(f"No se encontro el valor {valor6} en el conjunto.")

# //////// Ejercicio 7 ////////
print("\nEjercicio 7")

conjuntoA7Elementos = input("Ingrese numeros separados por ',' para el conjunto: ").split(",")
conjuntoA7 = set(int(num) for num in conjuntoA7Elementos)

agregarElementos = input("Ingrese tres numeros separados por ',' que quiera agregar al conjunto: ").split(",")
elementosAEnteros = set(int(num) for num in agregarElementos)

print(f"Conjunto: {conjuntoA7}")
print(f"Numeros a agregar: {elementosAEnteros}")

conjuntoA7.update(elementosAEnteros)

print(f"Conjunto nuevo: {conjuntoA7}")

# //////// Ejercicio 8 ////////
print("\nEjercicio 8")

print("Si es posible agregar elementos de una lista a un conjunto sin iterar.")

nuevaLista = ['a', 'b', 'c']
nuevoConjunto = {nuevaLista[0], nuevaLista[1], nuevaLista[2]}

print(f"Lista: {nuevaLista}")
print(f"Conjunto desde la lista sin utilizar iteraciones: {nuevoConjunto}")

# //////// Ejercicio 9 ////////
print("\nEjercicio 9")

cElementos = input("Ingrese numeros separados por ',' para el conjunto: ").split(",")
c = set(int(num) for num in cElementos)

unNumero = int(input("Ingrese el numero que quiere eliminar si esta en el conjunto: "))

print(f"Conjunto: {c}")
print(f"Numero a evaluar en el conjunto: {unNumero}")
c.discard(unNumero)
print(f"Conjunto: {c}")

# //////// Ejercicio 10 ////////
print("\nEjercicio 10")

cAElements = input("Ingrese numeros separados por ',' para el conjunto A: ").split(",")
cA = set(int(num) for num in cAElements)

cBElements = input("Ingrese numeros separados por ',' para el conjunto B: ").split(",")
cB = set(int(num) for num in cBElements)

if cA.issubset(cB) and cB.issubset(cA):
    print("El conjunto A es subconjunto de B y el conjunto B es subconjunto de A.")
elif cA.issubset(cB):
    print("El conjunto A es subconjunto de B.")
elif cB.issubset(cA):
    print("El conjunto B es subconjunto de A.")
else:
    print("Los conjuntos A y B son diferentes.")
