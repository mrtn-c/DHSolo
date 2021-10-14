'''Agregar infraestructura unit test al ejercicio anterior y comparar que la
comparación funciona para vehículos más lentos, más rápidos o igual develoces'''

from Vehiculo import *
from pytest import *

auto1 = Vehiculo("Audi")
auto1.set_velMax(300)
auto1.set_kmReco(2000)

auto2 = Vehiculo("Peugot")
auto2.set_velMax(200)
auto2.set_kmReco(2000)

assert (auto1 == auto2) == False
assert (auto1 > auto2) == True
assert (auto1 < auto2) == False

if (auto1==auto2):
    print("Tienen la misma velocidad maxima")
elif(auto1 > auto2):
    print("El primer auto es mas rapido")
elif (auto1 < auto2):
    print("El segundo auto es mas rapido")
    


