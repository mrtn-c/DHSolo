#Escribir un programa en Python que a partir de un string, separe en una lista todas las palabras que contengan una "a" y finalicen en "b"

import re

texto = "avberb si esto funcaab no lo se jab aab nose aaabx"

pattern = re.compile(r"\b.a.*b\b")

print("Se encontraron: ", pattern.findall(texto))