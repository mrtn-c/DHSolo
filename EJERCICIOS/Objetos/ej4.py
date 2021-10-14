'''Luego, crear una lista con 10 instancias Colectivo, 2 motocicleta, 3 ca-miones y 3 automóviles. Se debe recorrer la lista, invocar a los métodosarrancar y 
esperar un tiempo random. Finalmente, se debe volver a recorrer la lista, 
invocando los métodos frenare imprimir el tiempo de marcha de cada uno de los vehículos (diferenciade tiempos entre arrancar y frenar).9'''

from Vehiculos import *
import time
from random import *

from datetime import datetime, timedelta
from sys import stdout
from time import sleep


semaforo = [Camion(),Colectivo(),Moto(),Auto()]
flag = True
rnd = randint(3,7)
print(rnd)

print("Arranquen!!")

tempo = timedelta(seconds = rnd)
for movil in semaforo:
    movil.arrancar()

print(rnd)

while(str(tempo) != '0:00:00'):
    stdout.write("\r%s"%tempo)
    stdout.flush()
    tempo = tempo - timedelta(seconds=1)
    sleep(1)

print("\nFrenen!!")
for movil in semaforo:
    movil.frenar()
    movil.tiempo_de_marcha(rnd)
    print(movil.presentacion()+": "+str(movil.tiempo_de_marcha))

stdout.flush()
