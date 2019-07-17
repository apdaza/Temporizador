from Tkinter import *
from threading import *
from time import sleep
from temporizador import *

class InterfaceCronometros(Thread):

    def __init__(self):
        self.root = Tk()
        self.crono = Temporizador()
        #self.crono.cambiarEstado()
        self.frame = Frame(self.root)
        self.frame.pack()

        self.inicio = StringVar()
        self.inicio.set("00 : 00 : 00")
        self.text = Entry(self.frame, textvariable=self.inicio, font=("Helvetica", 15), justify='center')
        self.text.pack(side=TOP)

        self.cadena = StringVar()
        #self.display = Entry(self.frame, textvariable=self.cadena)
        self.display = Label(self.frame, textvariable=self.cadena, font=("Helvetica", 30))
        self.display.pack(side=TOP,padx=10,pady=10)

        self.buttonIniciar = Button(self.frame, text="Iniciar/Parar")
        self.buttonIniciar.bind("<Button-1>", self.cambio)
        self.buttonIniciar.pack(side=LEFT)


        self.buttonBorrar = Button(self.frame, text="Establecer")
        self.buttonBorrar.bind("<Button-1>", self.establecer)
        self.buttonBorrar.pack(side=RIGHT)

        Thread.__init__(self)
        self.start()

        self.root.mainloop()



    def cambio(self, event):
        self.crono.parado = not self.crono.parado

    def establecer(self, event):
        if self.inicio.get() == "":
            self.inicio.set("00 : 00 : 00")
        try:
            lista = [int(x) for x in self.inicio.get().split(" : ")]
        except:
            lista = [0,0,0]
            self.inicio.set("00 : 00 : 00")
        self.crono.iniciar(lista)
        #self.crono.borrar()

    def run(self):
        while True:
            if not self.crono.parado:
                self.crono.retroceder()
            sleep(0.5)
            self.cadena.set(self.crono.mostrar_tiempo())

    def callback(self):
        self.root.quit()


app = InterfaceCronometros()
