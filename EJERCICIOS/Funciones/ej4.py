#Escribir una función que reciba una lista y retorne una nueva lista con los elementos de la primera sin repeticiones

def listaSinRepetir(lista):
    sinRepetir = set (lista)

    return sinRepetir

lista = [1,2,2,3,4,5,5,6,10,11,12,12,12,12]
print("La lista es:", lista)
print("Sin nada repetido quedo: ", listaSinRepetir(lista))

