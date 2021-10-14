'''Escribir un programa en Python que lea un archivo linea a linea y almacenedicho contenido en una lista'''

try:
    file = open("EJERCICIOS/Archivos/eje3.txt", "r")
    lines = file.readlines()
    print(lines)
    file.close()
except:
    print("No se pudo abrir")