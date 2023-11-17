# //////// Ejercicio 14 ////////
print("\nEjercicio 14")

pizzasIngredientes = {"Pizza Vegetariana" : ["Pimientos", "Tofu"], "Pizza No Vegetariana" : ["Peperoni", "Jamon", "Salmon"]}

seleccion = input("Desea llevar una pizza vegetariana? (SI/NO): ").lower()

if seleccion == "si":
    elegirIngrediente = pizzasIngredientes["Pizza Vegetariana"]
    ingrediente = int(input(f"Ingrese el ingrediente que desea en la pizza: [1] {elegirIngrediente[0]} | [2] {elegirIngrediente[1]}: "))
    if ingrediente <= len(elegirIngrediente) and ingrediente > 0:
        print(f"Orden: Pizza Vegetariana - Ingredientes: Mozzarella, Tomate y {elegirIngrediente[ingrediente - 1]}.")
    else:
        print("Ingrediente invalido.")
elif seleccion == "no":
    elegirIngrediente = pizzasIngredientes["Pizza No Vegetariana"]
    ingrediente = int(input(f"Ingrese el ingrediente que desea en la pizza: [1] {elegirIngrediente[0]} | [2] {elegirIngrediente[1]} | [3] {elegirIngrediente[2]}: "))
    if ingrediente <= len(elegirIngrediente) and ingrediente > 0:
        print(f"Orden: Pizza No Vegetariana - Ingredientes: Mozzarella, Tomate y {elegirIngrediente[ingrediente - 1]}.")
    else:
        print("Ingrediente invalido.")
else:
    print("Opcion de pizza invalida.")