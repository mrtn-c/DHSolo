#4. Escribir un programa en Python que a partir de un string, veriﬁque cuales
#lineas del mismo contienen un signo +,-,*,/ y/o = en su interior.

import re

pattern = re.compile(r"[\+|\-|\*|\=|\/]+")

texto = '''hola - mal\n
q viniste jaja asi somos +\n
q loco esto /\n 
soy demasiado bueno para jugar al counter///===\n'''

lista = texto.split("\n")

for i in lista: 
    print(pattern.search(i))
  