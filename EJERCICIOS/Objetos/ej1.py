'''Crear una clase vehículo que contenga los atributos marca, velocidad máxi-ma y kilómetros recorridos. 
La marca debe ser ingresada en el constructory los demás atributos deben tener sus métodos getters y setters.'''

from Vehiculo import *

peugot = Vehiculo("Peugot")
peugot.set_velMax(int(input("Ingrese la velocidad maxima: ")))
peugot.set_kmReco(int(input("Ingrese los km recorridos: ")))


print("El vehiculo es marca: ",str(peugot.get_marca()), " \nSu velocidad maxima es: ", str(peugot.get_velMax()), " \nTiene ", str(peugot.get_kmReco()), "km recorridos")





    
    




        
        