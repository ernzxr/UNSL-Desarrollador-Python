# //////// Ejercicio 3 ////////
print('''
Ejercicio 3:''')

tuple3 = ('Soy', "inmutable", "no?", "si.")
#tuple3[3] = "no."
print(tuple3)
print('''tuple3[3] = "no." 
Dara un error ya que las tuplas no aceptan el metodo de reasignacion.''')

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