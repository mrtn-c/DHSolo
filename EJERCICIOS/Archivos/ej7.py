'''Escribir un programa en Python que lea información de texto de cuatro archivos distintos, la imprima por pantalla y luego la guarde en un archivo distinto.'''


file = open("EJERCICIOS/Archivos/texto1", "r")
filefinal = open("EJERCICIOS/Archivos/textoFinal", "w")
texto = file.read()
print(texto)
file.close()
filefinal.write(texto)

file = open("EJERCICIOS/Archivos/texto2", "r")

texto = file.read()
print(texto)
file.close()
filefinal.write(texto)

file = open("EJERCICIOS/Archivos/texto3", "r")
texto = file.read()
print(texto)
file.close()
filefinal.write(texto)
filefinal.close()

filefinal = open("EJERCICIOS/Archivos/textoFinal", "r")
texto = filefinal.read()

print("El texto final quedo como: ", texto)


juana     
karen
carolina
fiona
camila