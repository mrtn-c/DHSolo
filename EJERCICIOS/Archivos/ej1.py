'''Listar todos los modos de apertura de un archivo y extraer conclusionesde cada uno'''

try:
    file = open("EJERCICIOS//Archivos//texto.txt","w") #r solo lectura, r+ lectura y escritura, w solo escritura (si existe lo borra, si no crea), w+ ni usar, a sirve para agregar algo, a+ agrega y lee puntero al final del archivo
    file.write("jjajajajaja q onda\n")
    file.write("sisis bro")
    file.close()
    file = open("EJERCICIOS//Archivos//texto.txt","r")
    lines = file.readlines()
    for i in lines:
        print(i)
    file.close()
except:
    print("No se pudo abrir")