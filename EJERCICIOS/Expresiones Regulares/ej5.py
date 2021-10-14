'''Escribir un programa en Python que a partir de un string, extraiga lasfechas con formato dd/mm/yyyy'''

import re

texto = input("Ingrese un texto: ")

pattern = re.compile(r'\b\d{1,2}/\d{1,2}/\d{4,4}')

print(pattern.findall(texto))