'''Agregar al programa anterior el camino inverso'''

import json

file = open("EJERCICIOS/JSON/eje2.json","r")
data = json.load(file)

nombre = None
apellido = None
edad = 0
amigos = {}
hobbies = []

nombre = data["Nombre"]
apellido = data["Apellido"]
edad = data["Edad"]
amigos = data["Amigos"]
hobbies = data["Hobbies"]

print("Nombre: "+str(nombre)+"\n"+str(type(nombre)))
print("Apellido: "+str(apellido)+"\n"+str(type(apellido)))
print("Edad: "+str(edad)+"\n"+str(type(edad)))
print("amigos: "+str(amigos)+"\n"+str(type(amigos))+" ")
print("hobbies: "+str(hobbies)+"\n"+str(type(hobbies))+" ")
