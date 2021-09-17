'''Diseñar un programa que recibiendo el nombre de un archivo, permitaseparar el nombre de su extensión'''

archivo = input("Ingrese un archivo con su extension (recuerde el punto): ")
nombreArchivo = ""

for i in archivo:
    if(i == '.'):
        break
    nombreArchivo += i

print(nombreArchivo)

    
