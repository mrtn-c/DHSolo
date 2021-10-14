'''Escribir un programa en Python que permita convertir tipos de datos de Python a JSON'''

import json


try:
    file = open("EJERCICIOS/JSON/eje1.json", "r")
except:
    print("NO SE PUDO ABRIR")

data = json.load(file) 

nombre = "Martincho"
apellido = "Cometta"
edad = 10
amigos = ["Juan","Marcos","Juancito"]
hobbies = ["Correr","Nadar"]

if data["Nombre"] != nombre:
    data["Nombre"] = nombre

if data["Apellido"] != apellido:
    data["Apellido"] = apellido

if data["Edad"] != edad:
    data["Edad"] = edad

if data["Amigos"] != amigos:
    data["Amigos"] = amigos

if data["Hobbies"] != hobbies:
    data["Hobbies"] = hobbies

jsonstr = json.dumps(data)
file.close()
file = open("EJERCICIOS//JSON//eje1.json", "w")
file.write(jsonstr)
file.close()



