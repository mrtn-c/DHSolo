'''Definir una clase abstracta llamada vehículo con las interfaces arrancar(),frenar() y tiempo_de_marcha() 
Luego implementar las clases hijas:a) Colectivob) Motocicletac) Camiónd) Automóvil Implementar cada uno de los métodos heredados de la clase abstracta.'''

from abc import ABC, abstractmethod

class Vehiculos(ABC):

    tiempo_de_marcha = None
    
    @abstractmethod
    def arrancar(self):
        pass
    @abstractmethod
    def frenar(self):
        pass
    @abstractmethod
    def tiempo_de_marcha(self, time):
        pass

class Colectivo(Vehiculos):
    def arrancar(self):
        return super().arrancar()
    def frenar(self):
        return super().frenar()
    def tiempo_de_marcha(self, time):
        self.tiempo_de_marcha = time
    def presentacion(self):
        return "Colectivo"

class Moto(Vehiculos):
    def arrancar(self):
        return super().arrancar()
    def frenar(self):
        return super().frenar()
    def tiempo_de_marcha(self, time):
        self.tiempo_de_marcha = time
    def presentacion(self):
        return "Moto"

class Auto(Vehiculos):
    def arrancar(self):
        return super().arrancar()
    def frenar(self):
        return super().frenar()
    def tiempo_de_marcha(self, time):
        self.tiempo_de_marcha = time
    def presentacion(self):
        return "Auto"

class Camion(Vehiculos):
    def arrancar(self):
        return super().arrancar()
    def frenar(self):
        return super().frenar()
    def tiempo_de_marcha(self, time):
        self.tiempo_de_marcha = time
    def presentacion(self):
        return "Camion"

        
        
