class Vehiculo:
    """Se define un vehiculo"""
    ruedas = 4 #atributo de clase !! todos lo comparten
    
    def __init__(self,marca): #Self apunta a esta clase, como this. Es para tener atributos de instancia.
        self.__marca = marca

    def get_velMax(self):
        return self.__vel_max
    
    
    def set_velMax(self,vel_max):
        self.__vel_max = vel_max
      
    
    def get_kmReco(self):
        return self.__km_reco
    
    
    def set_kmReco(self,km_reco):
        self.__km_reco = km_reco
    
    def get_marca(self):
        return self.__marca

    def __eq__(self, other):
        return self.__vel_max > other.__vel_max

    def __str__(self):
        return "Marca: {}, Vel.Max: {}, Km.Reco: {}".format(self.__marca,self.__vel_max,self.__km_reco)
    
    def __gt__(self,other):
        return self.__vel_max > other.__vel_max
    
    def __lt__(self, other):
        return self.__vel_max < other.__vel_max
    

