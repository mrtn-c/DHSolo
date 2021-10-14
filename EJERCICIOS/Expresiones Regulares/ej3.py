#Escribir un programa en Python que a partir de un string, verifique sitodas las lineas del mismo contienen un ; al final.

import re

texto = """Hola bro;\n
que tal mi pana;\n
jeje\n
no se q mas\n""" 

lista = texto.split("\n")


pattern = re.compile(r".;$")

for i in lista:
    print(i)
    print(pattern.search(i))



