# //////// Ejercicio 3 ////////
print("\nEjercicio 3")

ln = []
addItems = int(input("Ingrese la cantidad de duplas que quiere ingresar: "))

for i in range(addItems):
    a3 = input(f"{i + 1}. Ingrese un nombre de clave: ")
    b3 = int(input(f"{i + 1}. Ingrese un valor numerico: "))
    ln.append((a3, b3))

dln = dict(ln)
print(dln)

# //////// Ejercicio 4 ////////
print("\nEjercicio 4")

addItems4 = int(input("Ingrese la cantidad de items a agregar al diccionario: "))
generatedDict = []
for i in range(addItems4):
    clave = input(f"{i + 1}. Ingrese un nombre de clave: ")
    valor = input(f"{i + 1}. Ingrese un valor: ")
    generatedDict.append((clave, valor))

d4 = dict(generatedDict)

e = input("Ingrese un elemento para buscar en los valores del diccionario: ")

if e in d4.values():
        print(f"Se encontraron {list(d4.values()).count(e)} veces al elemento `{e}` en el diccionario.")
else:
    print("No se encontro al elemento en el diccionario.")

# //////// Ejercicio 6 ////////
print("\nEjercicio 6")

generatedDict6 = []
agregarItems6 = int(input("Ingrese la cantidad de items que quiere agregar al diccionario: "))
for i in range(agregarItems6):
    clave6 = input(f"{i + 1}. Ingrese una clave: ")
    valor6 = input(f"{i + 1}. Ingrese un valor: ")
    generatedDict6.append((clave6, valor6))

d6 = dict(generatedDict6)

print(f"\nLista de tuplas clave y valor: {generatedDict6}")
print(f"Diccionario: {d6}")

# //////// Ejercicio 7 ////////
print("\nEjercicio 7")

generatedDict7 = [(int(input(f"{i + 1}. Ingrese DNI: ")), [input("Ingrese Nombre: "), input("Ingrese Domicilio: "), int(input("Ingrese Edad: "))]) for i in
                  range(3)]

d7 = dict(generatedDict7)
print(d7)

# //////// Ejercicio 12 ////////
print("\nEjercicio 12")

print('''No se pueden realizar rodajas en los diccionarios directamente,
se debe manipular el diccionario previamente antes de poder realizar este tipo
de operacion, como por ejemplo transformar en lista sus values, items o keys
y luego realizar la operacion de rodaja.''')

# //////// Ejercicio 13 ////////
print("\nEjercicio 13")

print('''No se pueden realizar zancadas en los diccionarios directamente,
se debe manipular el diccionario previamente antes de poder realizar este tipo
de operacion, como por ejemplo transformar en lista sus values, items o keys
y luego realizar la operacion de zancada.''')

# //////// Ejercicio 14 ////////
print("\nEjercicio 14")

agregarItems14a = int(input("a. Ingrese la cantidad de items a agregar para el diccionario #1: "))
d14a = dict((input(f"{i+1}. Ingrese una clave: "), (input(f"{i+1}. Ingrese un valor: "))) for i in range(agregarItems14a))

agregarItems14b = int(input("a. Ingrese la cantidad de items a agregar para el diccionario #2: "))
d14b = dict((input(f"{i+1}. Ingrese una clave: "), (input(f"{i+1}. Ingrese un valor: "))) for i in range(agregarItems14b))

print(f"Diccionario 1: {d14a}")
print(f"Diccionario 2: {d14b}")

u = d14a | d14b
print (f"Union de diccionarios: {u}")

i = {}
for j in d14a.keys():
    if j in d14b: ## and d14a[j] == d14b[j]: Evalua si la clave:valor de cada diccionario es exactamente igual.
        i[j] = d14a[j]
print(f"Interseccion de diccionarios: {i}")

diff1 = {clave: valor for clave, valor in d14a.items() if clave not in d14b}
diff2 = {clave: valor for clave, valor in d14b.items() if clave not in d14a}
print(f"Diferencia de los diccionarios #1 - #2: {diff1}")
print(f"Diferencia de los diccionarios #2 - #1: {diff2}")

ds = {clave: valor for clave, valor in d14a.items() if clave not in d14b}
ds.update({clave: valor for clave, valor in d14b.items() if clave not in d14a})
print(f"Diferencia simetrica de los diccionarios #1 y #2: {ds}")