# //////// Ejercicio 1 ////////
print('''
Ejercicio 1:''')

d = tuple([0, 0, 0])
a = (0,)
n = int(input("Ingrese la cantidad de 0 que quiere en la tupla: "))
tuple1 = (0,) * n

print(d)
print(a)
print(tuple1)

# //////// Ejercicio 2 ////////
print('''
Ejercicio 2:''')

op0 = (10,20)
op1 = (8,20)
r = tuple((x+y, x+y) for x, y in zip(op0, op1))
print(op0)
print(op1)
print(r)

# variable = ((op0[0]+op1[0]), (op1[1]+op1[1]))
# print(variable)

# //////// Ejercicio 3 ////////
print('''
Ejercicio 3:''')

tuple3 = ('Soy', "inmutable", "no?", "si.")
#tuple3[3] = "no."
print(tuple3)
print('''tuple3[3] = "no." 
Dara un error ya que las tuplas no aceptan el metodo de reasignacion.''')

# //////// Ejercicio 4 ////////
print('''
Ejercicio 4:''')

t = ([1, 2, 3, 4, 5])
print(t)
nMultiplication = int(input("Ingrese un numero para multiplicar la tupla actual: "))
t = tuple(map(lambda num: num * nMultiplication, t))
print(t)

# //////// Ejercicio 5 ////////
print('''
Ejercicio 5:''')

a5 = input("Ingrese un dato: ")
b5 = input("Ingrese otro dato: ")
c5 = input("Ingrese un ultimo dato: ")
tuple5 = (a5, b5, c5)
print(tuple5)

# //////// Ejercicio 6 ////////
print('''
Ejercicio 6''')

t6 = tuple((int(input(f"{i+1}. Ingrese un numero: "))) for i in range(4))
print(t6)

sumTuple = int(input("Ingrese un valor numerico para sumarle a cada elemento de la tupla: "))
s = tuple(map(lambda num: num + sumTuple, t6))
print(s)

resTuple = int(input("Ingrese un valor numerico para restarle a cada elemento de la tupla: "))
r = tuple(map(lambda num: num - resTuple, t6))
print(r)

print(f"Tuplas generadas: {t6}, {s}, {r}")

# //////// Ejercicio 7 ////////
print('''
Ejercicio 7''')

tuple7 = ("Ejercicio", 7)
print (f'''a. Para acceder a un elemento de una tupla podemos utilizar el metodo de corchetes, por ejemplo,
para la tupla: tuple7: {tuple7} podemos acceder a su segundo elemento utilizando tuple7[1]: {tuple7[1]}.
b. Si queremos acceder a un indice que no existe recibiremos un error de tipo IndexError.
c. La longitud de una tupla la podemos calcular utilizando la funcion len(), por ejemplo len(tuple7): {len(tuple7)}''')

# //////// Ejercicio 8 ////////
print('''
Ejercicio 8''')

tuple8 = tuple([(input(f"{i + 1}. Ingrese un elemento: ")) for i in range(2)])
a8, b8 = tuple8
print(f"Desempaquetado a: {a8}")
print(f"Desempaquetado b: {b8}")

# //////// Ejercicio 9 ////////
print('''
Ejercicio 9''')

a9 = [input(f"{i+1}. Ingrese un valor para la variable a: ") for i in range(2)]
b9 = [input(f"{i+1}. Ingrese un valor para la variable b: ") for i in range(2)]
tuple9 = tuple([a9, b9])
print(tuple9)

# //////// Ejercicio 10 ////////
print('''
Ejercicio 10''')

a10 = int(input("Ingrese un numero: "))
tuple10 = tuple((input("Ingrese los numeros que quiera separados por comas sin espacios: ")).split(","))
tuple10 = tuple(map(lambda num: int(num), tuple10))

print(tuple10)
print(a10 in tuple10)

# //////// Ejercicio 11 ////////
print('''
Ejercicio 11''')

a11 = int(input("Ingrese un numero: "))
tuple11 = tuple((input("Ingrese los numeros que quiera separados por comas sin espacios: ")).split(","))
tuple11 = tuple(map(lambda num: int(num), tuple11))

if (a11 in tuple11):
    print(f"El numero {a11} se encontro en el indice: {tuple11.index(a11)} de la tupla {tuple11}")
else:
    print("-1")

# //////// Ejercicio 12 ////////
print('''
Ejercicio 12''')

print(f'''a. El concepto de rodaja hace referencia a la operacion slicing en Python. Esta funcionabilidad nos permite
extraer una parte de un objeto iterable, como por ejemplo una tupla.
b. Las zancadas hacen referencia a una de la propiedades que tiene la funcion de slicing, el stride, que es el paso, lo que nos permite
a la hora de extraer la parte de un objeto iterable, en que saltos/pasos queremos que se seleccionen los elementos.
c. A continuacion se realizaran impresiones con los resultados practicos de lo explicado.
Teniendo la lista ("Hola", 1, 2, 3,"profesor"), se imprimira el slicing [:-4] para obtener un saludo general y el stride [::4] para saludarle :)!''')

tuple12 = ("Hola de nuevo!", 1, 2, 3,"profesor!")
saludos = tuple12[:1]
saludosProfe = tuple12[0::4]
print(tuple12)
print(saludos)
print(saludosProfe)

# //////// Ejercicio 13 ////////
print("\nEjercicio 13")

a13 = int(input("Ingrese un numero: "))
addElements = int(input("Ingrese la cantidad de numeros que desea agregar a la tupla: "))

tuple13 = tuple(int(input(f"{i+1}. Ingrese un numero: ")) for i in range(addElements))

if (tuple13.count(a13) == 1):
    print(f"{a13} se encontro 1 vez en la tupla.")
elif (tuple13.count(a13) > 1):
    print(f"{a13} se encontro {tuple13.count(a13)} veces en la tupla.")
else:
    print(f"No se encontro {a13} en la tupla.")

# //////// Ejercicio 14 ////////
print("\nEjercicio 14")

agregandoElementos = int(input("Ingrese la cantidad de elementos que desea agregar: "))
tuple14 = tuple((input(f"{i+1}. Ingrese el elemento: ")) for i in range(agregandoElementos))
e14 = input("Ingrese el elemento que desea buscar en la tupla: ")

if e14 in tuple14:
    print(f"{e14} se encuentra en la tupla.")
else:
    print(f"No se encontro {e14} en la tupla.")

# //////// Ejercicio 15 ////////
print("\nEjercicio 15")

addElementsToTuple = int(input("Ingrese la cantidad de elementos que desea agregar: "))
tuple15 = tuple((input(f"{i+1}. Ingrese el elemento: ")) for i in range(addElementsToTuple))
e15 = input("Ingrese el elemento que desea buscar en la tupla: ")

if e15 not in tuple15:
    print(f"No se encontro {e15} en la tupla.")
else:
    print(f"{e15} se encuentra en la tupla.")

# //////// Ejercicio 16 ////////
print("\nEjercicio 16")

addElementsToTuple1 = int(input("Ingrese la cantidad de elementos que desea agregar: "))
tuple16a = tuple((input(f"{i+1}. Ingrese el elemento: ")) for i in range(addElementsToTuple1))
print(tuple16a)

addElementsToTuple2 = int(input("Ingrese la cantidad de elementos que desea agregar: "))
tuple16b = tuple((input(f"{i+1}. Ingrese el elemento: ")) for i in range(addElementsToTuple2))
print(tuple16b)

array1 = list(tuple16a)
array2 = list(tuple16b)
array1.extend(array2)

newTuple = tuple(array1)
print(f"Concatenacion de la tupla a y tupla b: {newTuple}")

# //////// Ejercicio 17 ////////
print("\nEjercicio 17")

print("Ingrese cinco numeros, uno a la vez.")
tuple17 = tuple((int(input(f"{i+1}. Ingrese un numero: "))) for i in range(5))

sumaPares = 0
paresCheck = 0
sumaImpares = 0
imparesCheck = 0

for num in tuple17:
    if num % 2 == 0:
        sumaPares += num
        paresCheck = 1
    elif num % 2 != 0:
        sumaImpares += num
        imparesCheck = 1

if paresCheck == 1:
    print(f"La suma de los numeros pares es {sumaPares}.")
else:
    print("No se ingresaron numeros pares.")

if imparesCheck == 1:
    print(f"La suma de los numeros impares es {sumaImpares}.")
else:
    print("No se ingresaron numeros impares.")