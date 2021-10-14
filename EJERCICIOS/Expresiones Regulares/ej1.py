'''Escribir un programa en Python que verifique si una cadena de texto comienza con una palabra'''

import re

texto = input("Ingrese una frase: ")

pattern = re.compile(r'\bhola\b')

print(pattern.match(texto))

