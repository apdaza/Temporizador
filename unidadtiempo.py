class UnidadTiempo():
    def __init__(self):
        self.valor = 0
        self.tope = 0

    def iniciar(self, valor):
        self.valor = valor

    def retroceder(self):
        self.valor -= 1
        if self.valor < 0:
            self.valor = self.tope

    def reiniciar(self, valor):
        self.valor = valor

    def mostrar_valor(self):
        if self.valor < 10:
            return "0" + str(self.valor)
        return str(self.valor)

class Hora(UnidadTiempo):
    def __init__(self):
        self.valor = 0
        self.tope = 23

class Minuto(UnidadTiempo):
    def __init__(self):
        self.valor = 0
        self.tope = 59

class Segundo(UnidadTiempo):
    def __init__(self):
        self.valor = 0
        self.tope = 59
