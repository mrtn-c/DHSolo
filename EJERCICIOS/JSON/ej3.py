'''Escribir un programa en Python que permita leer información de un ar-chivo json y mostrarla por pantalla de forma ordenada'''

import json

file = open("EJERCICIOS/JSON/eje2.json", "r")

data = json.load(file)

print(str(data))