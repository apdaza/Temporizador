from unidadtiempo import *

class Temporizador():
    def __init__(self):
        self.hora = Hora()
        self.minuto = Minuto()
        self.segundo = Segundo()
        self.parado = True

    def iniciar(self, valores):
        self.hora.iniciar(valores[0])
        self.minuto.iniciar(valores[1])
        self.segundo.iniciar(valores[2])

    def retroceder(self):
        self.segundo.retroceder()
        if self.segundo.valor == self.segundo.tope:
            self.minuto.retroceder()
            if self.minuto.valor == self.minuto.tope:
                self.hora.retroceder()

    def reiniciar(self, valores):
        self.hora.iniciar(valores[0])
        self.minuto.iniciar(valores[1])
        self.segundo.iniciar(valores[2])

    def mostrar_tiempo(self):
        return str(self.hora.mostrar_valor()) + " : " + str(self.minuto.mostrar_valor()) + " : " + str(self.segundo.mostrar_valor())
