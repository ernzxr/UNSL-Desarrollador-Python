# Ejercicio 1

print('''
Ejercicio 1: ''')

intNumber = int(input("Ingrese un numero int: "))
print(intNumber)

# Ejercicio 2
print('''
Ejercicio 2: ''')

floatNumber = float(input("Ingrese un numero float: "))
print(floatNumber)

#Ejercicio 3
print('''
Ejercicio 3: ''')

number1 = int(input("Ingrese un numero: "))
number2 = int(input("Ingrese otro numero: "))

suma = number1 + number2
resta = number1 - number2
multiplicacion = number1 * number2

print(f'''Resultado suma: {suma}.
Resultado resta: {resta}.
Resultado multiplicacion: {multiplicacion}.''')

#Ejercicio 4
print('''
Ejercicio 4: ''')

base = int(input("Ingresa la base del triangulo: "))
height = int(input("Ingresa la altura del triangulo: "))
side2 = int(input("Ingresa el lado del triangulo que no sea la base: "))
side3 = int(input("Ingresa el segundo lado del triangulo que no sea la base: "))

perimeter = base + side2 + side3
area = (base * height) / 2

print(f'''El perimetro del triangulo es: {perimeter} cms.
El area del triangulo es: {area} cms^2.''')

#Ejercicio 5
print('''
Ejercicio 5: ''')

squareSide = int(input("Ingresa el lado de un cuadrado: "))

squarePerimeter = squareSide * 4
squareArea = squareSide ** 2

print(f'''El perimetro del cuadrado es: {squarePerimeter} cms.
El area del cuadrado es: {squareArea} cms.''')

#Ejercicio 6
print('''
Ejercicio 6: ''')

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))
num3 = int(input("Ingrese un numero: "))
num4 = int(input("Ingrese un numero: "))
num5 = int(input("Ingrese un numero: "))

promedio = (num1 + num2 + num3 + num4 + num5) / 5

print(f"El promedio de los numeros ingresados es: {promedio}.")

#Ejercicio 7
print('''
Ejercicio 7: ''')

print("Hola Mundo!")

#Ejercicio 8
print('''
Ejercicio 8: ''')

text = str(input("Ingrese un texto: "))

print(f"Texto introducido: {text}")

#Ejercicio 9
print('''
Ejercicio 9: ''')

s = str(input("Ingrese un texto: "))

print(s)

#Ejercicio 10
print('''
Ejercicio 10: ''')

nombre = str(input("Ingrese un nombre: "))

print("Hola:", nombre)

#Ejercicio 11
print('''
Ejercicio 11: ''')

name = str(input("Ingrese el nombre del trabajador: "))
workHours = int(input("Ingrese las horas trabajadas: "))
pricePerHour = float(input("Ingrese el precio por hora de trabajo: "))

salary = round((workHours * pricePerHour), 2)

print(f"El trabajador {name} debe cobrar {salary}$ por el trabajo realizado.")

#Ejercicio 12
print('''
Ejercicio 12: ''')

weightIMC = float(input("Ingrese el peso en kilogramos: "))
heightIMC = float(input("Ingrese la altura de la persona en metros: "))

IMC = round((weightIMC / (heightIMC ** 2)), 2)

print(f"El IMC de la persona es: {IMC}.")

#Ejercicio 13
print('''
Ejercicio 13: ''')

m = int(input("Ingrese un numero: "))
n = int(input("Ingrese un numero distinto de 0: "))

division = round((m / n), 2)
resto = m % n

print(f'''El cociente de la division entre {m} y {n} es: {division}.
El resto entre {m} y {n} es: {resto}.''')

#Ejercicio 14
print('''
Ejercicio 14: ''')

dolarToday = float(input("Ingrese la cotizacion del Dolar actual: "))
euroToday = float(input("Ingrese la cotizacion del Euro actual: "))
pesosAmount = round((float(input("Ingrese el monto en Pesos que quiere convertir a Dolar y Euro: "))), 2)

pesosToDolars = round((pesosAmount / dolarToday), 2)
pesosToEuros = round((pesosAmount / euroToday), 2)

print(f"{pesosAmount}$ Pesos equivalen a {pesosToDolars}$ Dolares y a {pesosToEuros}$ Euros.")

#Ejercicio 15
print('''
Ejercicio 15: ''')

inversion = round((float(input("Ingrese la cantidad de dinero que quiere invertir: "))), 2)
intereses = int(input("Ingrese la tasa de interes anual: "))
tiempo = int(input("Ingrese la cantidad de años de inversion: "))

gananciaTotal = round(((inversion + ((inversion * intereses) / 100)) * tiempo), 2)

print(f'''El capital que se obtendria de una inversion de {inversion}$ con una 
tasa de interes del {intereses}% por {tiempo} años es de: {gananciaTotal}$''')

#Ejercicio 16
print('''
Ejercicio 16: ''')

clows = int(input("Ingrese la cantidad de payasos vendidos: "))
dolls = int(input("Ingrese la cantidad de muñecas vendidas: "))

packageWeight = round(((clows * 112 + dolls * 75) / 1000), 2)

print("El peso del paquete a enviar es de:", packageWeight, "kgs.")

#Ejercicio 17
print('''
Ejercicio 17: ''')

inversionInicial = float(input("Ingrese la inversion inicial a realizar: "))

balance1 = round((inversionInicial + inversionInicial * 0.04), 2)
balance2 = round((balance1 + balance1 * 0.04), 2)
balance3 = round((balance2 + balance2 * 0.04), 2)

print(f'''El balance el primer año sera de {balance1}$,
del segundo año de {balance2}$
y del tercer año de {balance3}$.''')

#Ejercicio 18
print('''
Ejercicio 18: ''')

c = float(input("Ingrese una cantidad de dinero: "))
p = int(input("Ingrese el porcentaje a calcular: "))

porcentajeCalculado = round(((c * p) / 100), 2)

print(f'''El {p}% de {c}$ es: {porcentajeCalculado}$''')