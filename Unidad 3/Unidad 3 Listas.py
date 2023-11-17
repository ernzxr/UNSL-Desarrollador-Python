# //////// Ejercicio 1 ////////
print('''
Ejercicio 1:''')

array1 = [10, "hola", 2.5, 20, "que", 3.5, 30, "tal", 4.5]

print(array1[6])
print(array1[1])
print(array1[0:3])
print(array1[1::3])
print(array1[:1:-3])
print(array1[0::3])

# //////// Ejercicio 2 ////////
print('''
Ejercicio 2:''')

l = [0, 0, 0]
l2 = [0]

num = int(input("Ingrese un numero: "))

l3 = [0] * num
print(f'''l = {l} 
l2 = {l2}
l3 = {l3}''')

# //////// Ejercicio 3 ////////
print('''
Ejercicio 3:''')

l0 = [10, 20, 30]
l1 = [8, 20, 40]
r = []

for x, y in zip(l0, l1):
    r.append(x + y)
    print(x + y)

print(r)

# Alternativa
# r = [x + y for x, y in zip(l0, l1)]

# //////// Ejercicio 4 ////////
print('''
Ejercicio 4:''')

array4 = ["Hola", "Ernesto!"]
print(array4)
array4[1] = "Lucas!"
print(array4)

# //////// Ejercicio 5 ////////
print('''
Ejercicio 5:''')

t = [1, 2, 3, 4, 5]
n = int(input("Ingrese un numero: "))
array5 = [number * n for number in t]

print(array5)

# Alternativa
# array5a = []
# for number in t:
#     array5a.append(number * n)

# //////// Ejercicio 6 ////////
print('''
Ejercicio 6:''')

array6 = []
a = input("Ingrese el primer dato: ")
array6.append(a)
b = input("Ingrese el segundo dato: ")
array6.append(b)
c = input("Ingrese el tercer dato: ")
array6.append(c)

print(array6)

# //////// Ejercicio 7 ////////
print('''
Ejercicio 7:''')

l7 = []
for i in range(4):
    l7.append(int(input(f"{i+1}. Ingrese un numero: ")))
print(l7)

numberSum = int(input("Ingrese el numero con el que desea modificar la lista sumando: "))
s7 = [numero + numberSum for numero in l7]
print(s7)

numberRes = int(input("Ingrese el numero con el que desea modificar la lista restando: "))
r7 = [numero - numberRes for numero in l7]
print(r7)

tupla7 = (l7, s7, r7)
print(tupla7)

# //////// Ejercicio 8 ////////
print('''
Ejercicio 8:''')

array8 = ["Aprendiendo", "Python", "cafe", 1]
print(f'''Lista: ["Aprendiendo", "Python", "cafe", 1]
a. Para aprender programacion hace falta mucho: "{array8[2]}" == array8[2]
b. Si intentamos acceder a un indice inexistente en una lista recibimos el error "IndexError".
c. Para calcular la longitud de la lista se utiliza la funcion len(), en este caso len(array8) es igual a {len(array8)}.''')

# //////// Ejercicio 9 ////////
print('''
Ejercicio 9:''')

array9 = [input(f'''{index + 1}. Ingrese un dato: ''') for index in range(2)]
print(array9)
a9, b9 = array9
print(f'''Valor de la variable a : {a9}''')
print(f'''Valor de la variable b : {b9}''')

# //////// Ejercicio 10 ////////
print('''
Ejercicio 10:''')

a10 = input("a. Ingrese un valor: ")
b10 = input("b. Ingrese un valor: ")

empaquetar = []
empaquetar.append(a10)
empaquetar.append(b10)
resultado = tuple(empaquetar)
print(f"Se imprime la tupla resultado: {resultado} y se valida su tipo: {type(resultado)}")

# //////// Ejercicio 11 ////////
print('''
Ejercicio 11:''')

a11 = int(input("Ingrese un numero: "))
cantidadDeElementos = int(input("Ingrese la cantidad de numeros que desea agregar a la lista: "))

l11 = [int(input(f"{i+1}. Ingrese un numero: ")) for i in range(cantidadDeElementos)]

print (a11 in l11)

# //////// Ejercicio 12 ////////
print('''
Ejercicio 12:''')

a12 = int(input("Ingrese un numero: "))
addElements = int(input("Ingrese la cantidad de numeros que desea agregar a la lista: "))

l12 = [int(input(f"{i+1}. Ingrese un numero: ")) for i in range(addElements)]

if (a12 in l12):
    print(f"{a12} se encontro en el indice {l12.index(a12)} de la lista.")
else:
    print("-1")

# //////// Ejercicio 13 ////////
print('''
Ejercicio 13:''')

print(f'''a. El concepto de rodaja hace referencia a la operacion slicing en Python. Esta funcionabilidad nos permite
extraer una parte de un objeto iterable, como por ejemplo un string.
b. Las zancadas hacen referencia a una de la propiedades que tiene la funcion de slicing, el stride, que es el paso, lo que nos permite
a la hora de extraer la parte de un objeto iterable, en que saltos/pasos queremos que se seleccionen los elementos.
c. A continuacion se realizaran impresiones con los resultados practicos de lo explicado.
Teniendo la lista ["Hola", 1, 2, 3,"profesor"], se imprimira el slicing [:-4] para obtener un saludo general y el stride [::4] para saludarle :)!''')

array13 = ["Hola", 1, 2, 3,"profesor!"]
saludo = array13[:-4]
saludando = array13[::4]
print(saludo)
print(saludando)

# //////// Ejercicio 14 ////////
print('''
Ejercicio 14:''')

a14 = int(input("Ingrese un numero: "))
addingElements = int(input("Ingrese la cantidad de numeros que desea agregar a la lista: "))

l14 = [int(input(f"{i+1}. Ingrese un numero: ")) for i in range(addingElements)]

if (a14 in l14 and l14.count(a14) > 1):
    print(f"{a14} aparece {l14.count(a14)} veces en la lista.")
elif (a14 in l14):
    print(f"{a14} aparece {l14.count(a14)} vez en la lista.")
else:
    print("-1")

# //////// Ejercicio 15 ////////
print('''
Ejercicio 15:''')

l15 = [34, 3.2, 'Juan', 'Pedro',-2]
l15.append(str(input("Ingrese un string que desee agregar a la lista: ")))
verify = input("Ingrese el dato que desea saber cuantas veces se repite en la lista: ")

if (l15.count(verify)):
    print(f"{verify} se encontro en la lista en un total de veces: {l15.count(verify)}")
else:
    print("No se encontro el elemento.")

addElementsCount = int(input("Ingrese la cantidad de elementos que desea agregar a un nuevo array: "))
s15 = [input(f"{i+1}. Ingrese el elemento que desea agregar: ") for i in range(addElementsCount)]
l15.extend(s15)
print(l15)

l15.reverse()
print(f"Lista invertida: {l15}")

# //////// Ejercicio 16 ////////
print('''
Ejercicio 16:''')

elementsToAdd = int(input("Ingresa la cantidad de numeros que desea agregar a la lista: "))

l16 = [int(input(f"{i + 1}. Ingrese un numero: ")) for i in range(elementsToAdd)]
l16.sort()
arrayMax = max(l16)
arrayMin = min(l16)
print(f"La lista ingresada es {l16}, el maximo numero es el {arrayMax} y el minimo el {arrayMin}.")

# //////// Ejercicio 17 ////////
print('''
Ejercicio 17:''')

agregarElementosALista = int(input("Ingresa la cantidad de elementos que desea agregar a la lista: "))

l17 = [int(input(f"{i + 1}. Ingrese el elemento: ")) for i in range(agregarElementosALista)]

print(f"Lista creada: {l17}")

e17 = input('Ingrese un elemento para asignarle a la variable "e": ')
p17 = int(input("Ingrese un indice valido dentro de la longitud de la lista creada: "))

if (p17 < len(l17)) :
    l17.insert(p17, e17)
    print(f"Se inserto el elemento {e17} en la posicion {p17}: {l17}")
else:
    print("El indice ingresado no es valido.")