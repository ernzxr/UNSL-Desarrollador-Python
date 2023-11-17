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

# //////// Ejercicio 8 ////////
print("\nEjercicio 8")

print("Si es posible agregar elementos de una lista a un conjunto sin iterar.")

nuevaLista = ['a', 'b', 'c']
nuevoConjunto = {nuevaLista[0], nuevaLista[1], nuevaLista[2]}

print(f"Lista: {nuevaLista}")
print(f"Conjunto desde la lista sin utilizar iteraciones: {nuevoConjunto}")

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
