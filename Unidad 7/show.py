class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.children = []

    def recorridoSimetrico(self):
        result = []

        # Recorrer el primer hijo en simétrico
        if self.children:
            result.extend(self.children[0].recorridoSimetrico())

        # Agregar el valor del nodo actual al resultado
        result.append(self.valor)

        # Recorrer los hijos restantes en simétrico
        for i in range(1, len(self.children)):
            result.extend(self.children[i].recorridoSimetrico())

        return result

    def recorridoPostOrden(self):
        result = []

        # Recorrer los hijos en postorden
        for child in self.children:
            result.extend(child.recorridoPostOrden())

        # Agregar el valor del nodo actual al resultado
        result.append(self.valor)

        return result

    def recorridoPreOrden(self):
        result = []

        # Agregar el valor del nodo actual al resultado
        result.append(self.valor)

        # Recorrer los hijos en preorden
        for child in self.children:
            result.extend(child.recorridoPreOrden())

        return result

root = Nodo(1)
root.children.append(Nodo(2))
root.children.append(Nodo(3))
root.children.append(Nodo(4))
root.children[0].children.append(Nodo(5))
root.children[0].children.append(Nodo(6))
root.children[1].children.append(Nodo(7))
root.children[2].children.append(Nodo(8))

print(f"Orden Simetrico: {root.recorridoSimetrico()}")
print(f"Post Orden: {root.recorridoPostOrden()}")
print(f"Pre Orden: {root.recorridoPreOrden()}\n")

root.children[2].children.append(Nodo(9))
print(f"Orden Simetrico: {root.recorridoSimetrico()}")
print(f"Post Orden: {root.recorridoPostOrden()}")
print(f"Pre Orden: {root.recorridoPreOrden()}")