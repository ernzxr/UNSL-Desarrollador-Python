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
a, b = array9
print(f'''Valor de la variable a : {a}''')
print(f'''Valor de la variable b : {b}''')

# //////// Ejercicio 10 ////////
print('''
Ejercicio 10:''')

a10 = input("a. Ingrese un valor: ")
b10 = input("b. Ingrese un valor: ")

empaquetar = [a10, b10]
resultado = tuple(empaquetar)
print(f"Se imprime la tupla resultado: {resultado} y se valida su tipo: {type(resultado)}")

# //////// Ejercicio 12 ////////
print('''
Ejercicio 12:''')

a12 = int(input("Ingrese un numero: "))
addElements = int(input("Ingrese la cantidad de numeros que desee agregar a la lista: "))

l12 = [int(input(f"{i+1}. Ingrese un numero: ")) for i in range(addElements)]

if (a12 in l12):
    print(f"{a12} se encontro en el indice {l12.index(a12)} de la lista.")
else:
    print("-1")

# //////// Ejercicio 15 ////////
print('''
Ejercicio 15:''')

l15 = [34, 3.2, 'Juan', 'Pedro',-2]
l15.append(str(input("Ingrese un string que desee agregar a la lista: ")))
verify = eval(input("Ingrese el dato que desea saber cuantas veces se repite en la lista: "))

if (l15.count(verify)):
    print(f"{verify} se encontro en la lista en un total de veces: {l15.count(verify)}")
else:
    print("No se encontro el elemento.")

addElementsCount = int(input("Ingrese la cantidad de elementos que desea agregar a un nuevo array para incorporarlo a la lista anterior: "))
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

l17 = [input(f"{i + 1}. Ingrese el elemento: ") for i in range(agregarElementosALista)]

print(f"Lista creada: {l17}")

e17 = input('Ingrese un elemento para asignarle a la variable "e": ')
p17 = int(input(f"Ingrese un indice valido dentro de la longitud de la lista creada: "))

if (p17 < len(l17)) :
    l17.insert(p17, e17)
    print(f"Se inserto el elemento {e17} en la posicion {p17}: {l17}")
else:
    print("El indice ingresado no es valido.")