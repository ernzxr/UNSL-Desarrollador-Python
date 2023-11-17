class ContadorLimitado:
    def __init__(self, numero):
        self.maximo = 10
        self.inicializacion = self.validarInicializacion(numero)

    def getValorActual(self):
        return self.inicializacion

    def setIncrementar(self):
        if self.inicializacion == self.maximo:
            print(f"Valor maximo alcanzado: {self.maximo}")
        else:
            self.inicializacion += 1
            print(self.getValorActual())

    def validarInicializacion(self, numero):
        if numero >= self.maximo:
            print("El valor ingresado supera el maximo permitido.")
            print("Se inicializa el programa en 0.")
            return 0
        else:
            return numero


def ejercicio12():
    contador = ContadorLimitado(11)
    print(contador.getValorActual())
    for i in range(11):
        contador.setIncrementar()


ejercicio12()