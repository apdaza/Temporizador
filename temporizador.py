class Temporizador():
    def __init__(self):
        self.hora = Hora()
        self.minuto = Minuto()
        self.segundo = Segundo()

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
