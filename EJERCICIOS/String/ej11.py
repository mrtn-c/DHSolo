'''Detectar si una palabra ingresada es palindromo o no'''

palabra = input("Ingrese una palabra para ver si es palindroma: ")
indice_vuelta = len(palabra)-1
palindromo = True

for i in palabra:
    if(i == palabra[indice_vuelta]):
        indice_vuelta -= 1
        continue
    else:
        palindromo = False
        break

if (palindromo == True):
    print("La palabra es palindromo")
else:
    print("La palabra no es palindromo")