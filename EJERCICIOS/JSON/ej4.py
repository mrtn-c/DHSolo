'''Escribir un programa en Python que permita leer información de un tres json, las combine y lo almacene en toda en un cuarto archivo'''

import json

todo = dict()

file = open("EJERCICIOS/JSON/primero.json","r")
data = json.load(file)
todo.update({"Nombre":data["Nombre"]})
file.close()

file = open("EJERCICIOS/JSON/segundo.json","r")
data = json.load(file)
todo.update({"Apellido":data["Apellido"]})
file.close()

file = open("EJERCICIOS/JSON/tercero.json","r")
data = json.load(file)
todo.update({"Edad":data["Edad"]})
file.close()

file = open("EJERCICIOS/JSON/todo.json","w")
jsonstr = json.dumps(todo)
file.write(jsonstr)
file.close()