'''Modificar el programa anterior para que imprima la frecuencia de repeti-ción de cada palabra en el archivo'''

file = open("EJERCICIOS/Archivos/eje5.txt", "r")
lineas = file.readlines()

palabras = dict()

for line in lineas:
    for palabra in line.split():
        if palabras.get(palabra) == None:
            palabras.update({palabra:1})
        else:
            palabras.update({palabra:palabras.get(palabra)+1})

file.close()

print("La palabras se encuentran: ", palabras)
