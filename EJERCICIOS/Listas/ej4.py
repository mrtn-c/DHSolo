'''Diseñar un programa que dada una lista con números positivos y negativos,sustituya los negativos por cero'''

import random

lista = []

for i in range(30):
    lista.append(random.randint(-20,20))

print("La lista es: ", lista)

for i, valor in enumerate(lista):
    if valor < 0:
        lista[i]=0

print("La lista quedo: ", lista)


