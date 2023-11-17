nombreDeArchivo4 = input("Ingrese un nombre de archivo para abrirlo: ")

with open(nombreDeArchivo4, "r") as archivo:
    lineas = archivo.readlines()

    for linea in lineas:
        indiceLinea = lineas.index(linea)
        print(linea)
        palabras = linea.split()
        print(palabras)
        palabrasInvertidas = [palabra[::-1] for palabra in palabras]
        print(palabrasInvertidas)
        lineas[indiceLinea] = " ".join(palabrasInvertidas) + "\n"

with open(nombreDeArchivo4, "w") as archivo:
    archivo.writelines(lineas)
    print("El archivo ha sido modificado exitosamente.")