# //////// Ejercicio 1 ////////
print("\nEjercicio 1")

num = int(input("Ingrese un numero para verificar si es par o impar: "))

if num % 2 == 0:
    print("El numero ingresado es par.")
else:
    print("El numero ingresado es impar.")

# //////// Ejercicio 2 ////////
print("\nEjercicio 2")

n = input("Ingrese un numero para verificar si es capicua: ")
nInverted = n[::-1]

if n == nInverted and len(n) > 1:
    print("El numero es capicua.")
else:
    print("El numero no es capicua.")

# //////// Ejercicio 3 ////////
print("\nEjercicio 3")

opcion = (input("Elija una opcion: [A] Calcular perimetro | [B] Calcular area: ")).lower()

if opcion == "a":
    trianguloLados = input("Ingrese los lados del triangulo separados por coma para calcular su perimetro: ").split(",")
    perimetroTriangulo = sum(int(num) for num in trianguloLados)
    print(f"El perimetro del triangulo es: {perimetroTriangulo}")
elif opcion == "b":
    trianguloBaseAltura = input("Ingrese la base y altura del triangulo separados por coma: ").split(",")
    base = int(trianguloBaseAltura[0])
    altura = int(trianguloBaseAltura[1])
    areaTriangulo = (base * altura) / 2
    print(f"El area del triangulo es: {areaTriangulo}")
else:
    print("Ingrese una opcion valida.")

# //////// Ejercicio 4 ////////
print("\nEjercicio 4")

print('Teniendo una ecuacion cuadratica de tipo "ax^2 + bx + c')

a = float(input("Ingrese el coeficiente a de la ecuación: "))
b = float(input("Ingrese el coeficiente b de la ecuación: "))
c = float(input("Ingrese el coeficiente c de la ecuación: "))

discriminante = b ** 2 - 4 * a * c

if discriminante > 0:
    print("La ecuación tiene dos soluciones reales distintas.")
elif discriminante == 0:
    print("La ecuación tiene una única solución real.")
else:
    print("La ecuación no tiene solución real.")

# //////// Ejercicio 5 ////////
print("\nEjercicio 5")

opciones = int(input('''Elija una operacion a realizar: 
[1] Multiplicacion | [2] Division 
[3] Suma           | [4] Resta
Opcion: '''))

valoresAOperar = input("Ingrese dos numeros para operar separados por coma: ").split(",")
valor1 = int(valoresAOperar[0])
valor2 = int(valoresAOperar[1])

if opciones == 1:
    resultado = valor1 * valor2
    print(f"{valor1} * {valor2} = {resultado}")
elif opciones == 2:
    resultado = valor1 / valor2
    print(f"{valor1} / {valor2} = {resultado}")
elif opciones == 3:
    resultado = valor1 + valor2
    print(f"{valor1} + {valor2} = {resultado}")
elif opciones == 4:
    resultado = valor1 - valor2
    print(f"{valor1} - {valor2} = {resultado}")
else:
    print("Ingrese una opcion valida.")

# //////// Ejercicio 6 ////////
print("\nEjercicio 6")

equipos = input("Ingrese el nombre de los dos equipos separados por coma: ").split(",")

partido = {equipo: None for equipo in equipos}

resultadoEquipo1 = int(input(f"Ingrese el resultado del equipo {equipos[0]}: "))
partido[equipos[0]] = resultadoEquipo1

resultadoEquipo2 = int(input(f"Ingrese el resultado del equipo {equipos[1]}: "))
partido[equipos[1]] = resultadoEquipo2

if partido[equipos[0]] > partido[equipos[1]]:
    print(f"El equipo {equipos[0]} gano!")
elif partido[equipos[0]] < partido[equipos[1]]:
    print(f"El equipo {equipos[1]} gano!")
else:
    print("Los equipos empataron!")

# //////// Ejercicio 7 ////////
print("\nEjercicio 7")

leyMayorEdad = int(input("Mayor de edad por Ley: "))
edadUsuario = int(input("Ingrese su edad: "))

if edadUsuario >= leyMayorEdad:
    print("El usuario es mayor de edad")
else:
    print("El usuario es menor de edad.")

# //////// Ejercicio 8 ////////
print("\nEjercicio 8")

clave = input("Ingrese una contraseña: ")
ingreseClave = input("Reingrese la clave: ")

if clave == ingreseClave:
    print("Las contraseñas coinciden.")
else:
    print("Las contraseñas no coinciden.")

# //////// Ejercicio 9 ////////
print("\nEjercicio 9")

edadYSalario = input("Ingrese su edad y salario separado por una coma: ").split(",")
edadCheck = int(edadYSalario[0])
salarioCheck = int(edadYSalario[1])

print("El usuario debe tributar." if edadCheck > 16 and salarioCheck > 1000 else "No debe tributar.")

# //////// Ejercicio 10 ////////
print("\nEjercicio 10")

abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
              'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

nombre = input("Ingrese su nombre: ").lower()
sexo = input("Ingrese su sexo [F] | [M]: ").lower()

if nombre[0] in abecedario[:11] and sexo == "f":
    print("Pertenece al grupo A.")
elif nombre[0] in abecedario[14:] and sexo == "m":
    print("Pertenece al grupo A.")
else:
    print("Pertenece al grupo B.")

if abecedario.index(nombre[0]) < abecedario.index("m") and sexo == "f":
    print("Pertenece al grupo A.")
elif abecedario.index(nombre[0]) > abecedario.index("n") and sexo == "m":
    print("Pertenece al grupo A.")
else:
    print("Pertenece al grupo B.")

if (nombre < "m" and sexo == "f") or (nombre > "n" and sexo == "m"):
    print("Pertenece al grupo A.")
else:
    print("Pertenece al grupo B.")

# //////// Ejercicio 11 ////////
print("\nEjercicio 11")

tramosImpositivos = {1: "5%", 2: "15%", 3: "20%", 4: "30%", 5: "45%"}

rentaAnual = int(input("Ingrese su renta anual: "))

if rentaAnual < 10000:
    print(f"Le corresponde un tipo impositivo del {tramosImpositivos[1]}")
elif 10000 <= rentaAnual < 20000:
    print(f"Le corresponde un tipo impositivo del {tramosImpositivos[2]}")
elif 20000 <= rentaAnual < 35000:
    print(f"Le corresponde un tipo impositivo del {tramosImpositivos[3]}")
elif 35000 <= rentaAnual <= 60000:
    print(f"Le corresponde un tipo impositivo del {tramosImpositivos[4]}")
else:
    print(f"Le corresponde un tipo impositivo del {tramosImpositivos[5]}")

# //////// Ejercicio 12 ////////
print("\nEjercicio 12")

puntuacion = float(input("Ingrese la puntuacion obtenida: "))

if puntuacion < 0.4:
    dinero = 2400 * 0.0
    print(f'Nivel de rendimiento "Inaceptable" - Dinero a recibir {dinero}$')
elif 0.4 <= puntuacion < 0.6:
    dinero = 2400 * 0.4
    print(f'Nivel de rendimiento "Aceptable" - Dinero a recibir {dinero}$')
else:
    dinero = 2400 * puntuacion
    print(f'Nivel de rendimiento "Meritorio" - Dinero a recibir {dinero}$')

# //////// Ejercicio 13 ////////
print("\nEjercicio 13")

edadCliente = int(input("Ingrese su edad: "))

if edadCliente < 4:
    print(f"Entrada gratuita.")
elif 4 <= edadCliente <= 18:
    print(f"Debe abonar $5 la entrada.")
else:
    print("Debe abonar 10$ la entrada.")

# //////// Ejercicio 14 ////////
print("\nEjercicio 14")

pizzasIngredientes = {"Pizza Vegetariana": ["Pimientos", "Tofu"],
                      "Pizza No Vegetariana": ["Peperoni", "Jamon", "Salmon"]}

seleccion = input("Desea llevar una pizza vegetariana? (SI/NO): ").lower()

if seleccion == "si":
    elegirIngrediente = pizzasIngredientes["Pizza Vegetariana"]
    ingrediente = int(input(
        f"Ingrese el ingrediente que desea en la pizza: [1] {elegirIngrediente[0]} | [2] {elegirIngrediente[1]}: "))
    if len(elegirIngrediente) >= ingrediente > 0:
        print(f"Orden: Pizza Vegetariana - Ingredientes: Mozzarella, Tomate y {elegirIngrediente[ingrediente - 1]}.")
    else:
        print("Ingrediente invalido.")
elif seleccion == "no":
    elegirIngrediente = pizzasIngredientes["Pizza No Vegetariana"]
    ingrediente = int(input(
        f"Ingrese el ingrediente que desea en la pizza: "
        f"[1] {elegirIngrediente[0]} | [2] {elegirIngrediente[1]} | [3] {elegirIngrediente[2]}: "))
    if len(elegirIngrediente) >= ingrediente > 0:
        print(f"Orden: Pizza No Vegetariana - Ingredientes: Mozzarella, Tomate y {elegirIngrediente[ingrediente - 1]}.")
    else:
        print("Ingrediente invalido.")
else:
    print("Opcion de pizza invalida.")
