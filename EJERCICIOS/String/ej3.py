'''modificar el programa para que reciba dos números enteros que permitandefinir el comienzo y el fin de caracteres a extraer del string original'''

str = input("Ingrese una frase ")
cond = True
pos1 = 0
pos2 = 0

while (cond):
    pos1 = int(input("Escoga un numero, esta sera la posicion comienzo del string: "))
    if (pos1 <= len(str)):
        break
    print("Se excedio el rango, intente de nuevo con un numero mas chico")

while (cond):
    pos2 = int(input("Escoga un numero, esta sera la posicion comienzo del string: "))
    if (pos2 <= len(str)):
        break
    print("Se excedio el rango, intente de nuevo con un numero mas chico")

if (pos1 > pos2):
    aux = pos1
    pos1 = pos2
    pos2 = aux

print(str[pos1-1:pos2])
