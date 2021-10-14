#Escribir un programa en Python que lea todas las lineas de un archivo de texto

try:
    file = open("EJERCICIOS/Archivos/eje3.txt", "r")
    print(file.read())
    file.close()
except:
    print("No se pudo abrir")
