'''Escribir un programa en Python lea el contenido de un archivo e identifique la palabra más larga de todo el archivo'''

file = open("EJERCICIOS/Archivos/eje5.txt", "r")
lineas = file.readlines()

palabra_mas_larga = " "

for line in lineas:
    for palabra in line.split():
        if len(palabra)>len(palabra_mas_larga):
            palabra_mas_larga = palabra

print("La palabra mas larga es: ", palabra_mas_larga)




