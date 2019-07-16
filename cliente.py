from temporizador import Temporizador
from time import sleep
 
t = Temporizador()

t.iniciar([0,1,15])

while True:
    tiempo = t.mostrar_tiempo()
    print tiempo
    sleep(0.5)
    if tiempo == "00 : 00 : 00":
        break
    t.retroceder()
