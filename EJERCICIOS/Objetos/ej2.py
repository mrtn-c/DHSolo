'''Agregar a la clase anterior agregar un método que permita comparar dos clases vehículo entre si. 
El atributo de comparación es la velocidad.También se debe agregar el método __str__ para que imprima informa-ción de la clase'''

from Vehiculo import *

auto1 = Vehiculo("Peugot")
auto1.set_velMax(300)
auto1.set_kmReco(2000)

auto2 = Vehiculo("Audi")
auto2.set_velMax(320)
auto2.set_kmReco(3000)

if (auto1 == auto2):
    print("Tienen la misma velocidad maxima!")
else:
    print("No tiene la misma velocidad maxima!")

print(auto1)