#Escribir un programa en Python que a partir de un string, extraiga todas las direcciones de mail en el mismo

import re

texto = """primeradireccion@hotmail.com\n
segundadireccion@hotmail.com\n
estanoeshotmail.com\n
tercera@gmail.com\n"""

lista = texto.split("\n")

pattern = re.compile(r"\w+@{1}.+\.\w+\b")

for i in lista:
    print(pattern.search(i))