# //////// Ejercicio 2 ////////
print("\nEjercicio 2")

n = input("Ingrese un numero para verificar si es capicua: ")
nInverted = n[::-1]

if n == nInverted and len(n) > 1:
    print("El numero es capicua.")
else:
    print("El numero no es capicua.")

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