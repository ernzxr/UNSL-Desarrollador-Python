# //////// Ejercicio 1 ////////
print("\nEjercicio 1")

a = {}
b = dict()

# //////// Ejercicio 2 ////////
print("\nEjercicio 2")

d2 = {1:"Daniel", 2:"Germán", 3:"Analía", 4:"José", 5:"Gabriel"}
print(f"d2[3]: {d2[3]}")
print(f"La longitud del diccionario es: {len(d2)}")
print(f"Claves: {d2.keys()}")
print(f"Valores: {d2.values()}")

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

# //////// Ejercicio 5 ////////
print("\nEjercicio 5")

d5 = {}
agregarItems = int(input("Ingrese la cantidad de items que desea agregar al diccionario: "))
for i in range(agregarItems):
    clave5 = input(f"{i + 1}. Ingrese una clave: ")
    valor5 = input(f"{i + 1}. Ingrese un valor: ")
    d5[clave5] = valor5

c = input("Ingrese un elemento para buscar en las claves del diccionario: ")

if c in d5.keys():
    print(f"La clave {c} existe en el diccionario.")
else:
    print("No existe la clave en el diccionario.")

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

# //////// Ejercicio 8 ////////
print("\nEjercicio 8")

d8 = {"Tipo":"Diccionario","Mutabilidad":False}
print(f"Diccionario: {d8}")
d8["Mutabilidad"] = True
print(f'd8["Mutabilidad] = True')
print(f"Diccionario Mutable: {d8}")

# //////// Ejercicio 9 ////////
print("\nEjercicio 9")

print('''a. Un diccionario en Python es una estructura de datos que permite
almacenar pares de datos clave-valor. Cada clave es unica, los diccionarios
son mutables y no estan ordenados.
b. Si intentamos acceder a una clave que no existe sin utilizar los metodos
`in` o `get()` vamos a recibir un error de KeyError.
c. La longitud de un diccionario se puede obtener utilizando la funcion len().''')

# //////// Ejercicio 10 ////////
print("\nEjercicio 10")

addItems10 = int(input("Ingrese la cantidad de items que desea agregar al diccionario: "))
d10 = dict((input(f"{i+1}. Ingrese una clave: "),input(f"{i+1}. Ingrese un valor: ")) for i in range(addItems10))
a10 = input("a. Ingrese un valor para ser buscado en el diccionario: ")
b10 = input("b. Ingrese otro valor para ser buscado en el diccionario: ")

if a10 in d10.values():
    print(f"a. {a10} se encontro en el diccionario.")
else:
    print(f"a. No se encontro {a10} en el diccionario.")

if b10 in d10.values():
     print(f"b. {b10} se encontro en el diccionario.")
else:
     print(f"b. No se encontro {b10} en el diccionario.")

# //////// Ejercicio 11 ////////
print("\nEjercicio 11")

d11 = {}
a11 = int(input("Ingrese una clave numerica: "))

agregarItems11 = int(input("Ingrese la cantidad de elementos que desea agregar a la tupla: "))
t11 = tuple((input(f"{i+1}. Ingrese un elemento: ")) for i in range(agregarItems11))
d11[a11] = t11

print(d11)

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
    if j in d14b and d14a[j] == d14b[j]:
        i[j] = d14a[j]
print(f"Interseccion de diccionarios: {i}")

diff1 = {clave: valor for clave, valor in d14a.items() if clave not in d14b}
diff2 = {clave: valor for clave, valor in d14b.items() if clave not in d14a}
print(f"Diferencia de los diccionarios #1 - #2: {diff1}")
print(f"Diferencia de los diccionarios #2 - #1: {diff2}")

ds = {clave: valor for clave, valor in d14a.items() if clave not in d14b}
ds.update({clave: valor for clave, valor in d14b.items() if clave not in d14a})
print(f"Diferencia simetrica de los diccionarios #1 y #2: {ds}")