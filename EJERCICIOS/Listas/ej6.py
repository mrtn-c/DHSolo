'''Diseñar un programa que tomando una lista de números enteros, genere una nueva eliminando los números repetidos de la primera'''

lista = []
lista_no_rep = set() #El set es una lista pero sin elementos iguales. update() o add() para agregar algo nuevo (QUE NO ESTE YA DENTRO).

while True:
    x = input("Ingrese un numero entero: ")
    if (x>='0' and x<='9'):
        lista.append(int(x))
        lista_no_rep.add(int(x))
    else:
        break

print("La lista que ingreso fue: ", lista)
print("La lista sin nada repetido es:  ", lista_no_rep)

