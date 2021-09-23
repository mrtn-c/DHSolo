'''Crear una lista con 100 números aleatorios, luego se debe generar dos listasmás: una que contenga los números pares de la primera y otra los impares'''

import random

def cargarLista():
    lista = [] 
    for i in range(100):
        lista.append(random.randint(0,1000))
    return lista

lista = cargarLista()

listaPar = []
listaImpar = []

aux = 0

for i in lista:
    aux += 1
    if (i % 2 == 0):
        listaPar.append(i)
    else:
        listaImpar.append(i)

print(aux)

print("Numeros pares: \n- ")
for i in listaPar:
    print(i, "- ")

print("Numeros impares: \n- ")
for i in listaImpar:
    print(i, "- ")

