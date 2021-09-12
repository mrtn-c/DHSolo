'''Recibir por teclado un string y contar la cantidad de mayúsculas, minús-culas y símbolos que se encuentran en la misma'''

str = input("Ingrese una fraseee: ")
mayus = 0
minus = 0
simb = 0

for i in str:
    if (i >= 'a' and i <= 'z'):
        minus+= 1
    elif(i >= 'A' and i <= 'Z'):
        mayus+=1
    else:
        if (i == " "):
            continue
        simb+=1

print("Se encontraron\n\n Mayusculas: ", mayus, "\n\n Minusculas: ", minus, "\n\n Simbolos: ", simb)