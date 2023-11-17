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

#Ejercicio 13
print('''
Ejercicio 13: ''')

m = int(input("Ingrese un numero: "))
n = int(input("Ingrese un numero distinto de 0: "))

division = round((m / n), 2)
resto = m % n

print(f'''El cociente de la division entre {m} y {n} es: {division}.
El resto entre {m} y {n} es: {resto}.''')

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