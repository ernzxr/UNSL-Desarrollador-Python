import sys

print('''
Ejercicio 1:

He realizado la instalacion de Python en la carpeta "C:\\Users\\ernzxr\\AppData\\Local\\Programs\\Python\\Python311" 
y estoy utilizando PyCharm Community Edition 2023.1.1 para realizar los ejercicios.

Ejercicio 2:

El intérprete de Python es un programa informático que lee y ejecuta el código fuente escrito en el lenguaje de 
programación Python. Funciona como un intermediario entre el código escrito por los programadores y la máquina 
en la que se ejecuta.
Cuando se escribe un programa en Python y se ejecuta, el interprete se encarga de traducir y ejecutar cada instruccion
una a la vez. Analiza el codigo linea por linea y realiza las acciones necesarias para llevar a cabo las operaciones
indicadas.

Ejercicio 3:
''')

print("Hola Mundo")

print('''
Ejercicio 4:
''')

print("Hola", sys.argv[0])

print('''
Ejercicio 5:
''')

print(sys.argv)

if len(sys.argv) == 1:
    print("El programa no contiene scripts ni módulos.")

elif sys.argv[1] == "-":
    print('El programa se ha invocado con "-".')

elif sys.argv[1] == "-c":
    print('El programa se ha invocado con un comando "-c".')
    if sys.argv[2]:
        print(f"El comando ingresado es: {sys.argv[2]}.")
    else:
        print("Pero no se ha ingresado comando alguno.")

elif sys.argv[1] == "-m":
    print('El programa se ha invocado con un modulo "-m".')
    if sys.argv[2]:
        print(f"El modulo es: {sys.argv[2]}.")
    else:
        print("Pero no se ha ingresado modulo alguno.")

print('''
Ejercicio 6:
''')

heightTriangle = 20
baseTriangle = 10
areaTriangle = (baseTriangle * heightTriangle) / 2
print(f"El area de un triangulo de base 10cm y altura 20cm es: {int(areaTriangle)}cm.")

sideSquare = 40
areaSquare = sideSquare ** 2
print(f"El area de un cuadrado de 40cm por lado es: {areaSquare}cm.")

sideEquilateralTriangle = 20
perimeterTriangle = sideEquilateralTriangle * 3
print(f"El perimetro de un triangulo equilatero de 20cm por lado es: {perimeterTriangle}cm.")

heightRectangle = 35
widthRectangle = 60
perimeterRectangle = heightRectangle * 2 + widthRectangle * 2
print(f"El perimetro de un rectangulo de 35cm de alto por 60cm de ancho es: {perimeterRectangle}cm.")