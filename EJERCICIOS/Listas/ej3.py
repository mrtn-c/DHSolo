'''ingresar un string por teclado y hacer dos listas: una que contenga lasletras mayúsculas de la palabra y otra las minúsculas'''

frase = input("Ingrese una frase mi pana: ")

listaMin = []
listaMay = []

for i in frase:
    if ord(i)>96 and ord(i)<123:
        listaMin.append(i)
    elif ord(i)>64 and ord(i)<91:
        listaMay.append(i)

print("Minusculas: ", listaMin, "\nMayusculas: ", listaMay)


