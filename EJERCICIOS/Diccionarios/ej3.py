'''Borrar la key "veinte" su respectivo valor al ejercicio del apartado anterio'''

keys = ['Diez', 'Veinte', 'Treinta']
values = [10, 20, 30]

diccionario = dict()

for i in range(3):
    diccionario[keys[i]]=values[i]

print("1->El diccionario es: ",diccionario)

diccionario["Cuarenta"] = 40

print("2->El diccionario es: ",diccionario)

diccionario.pop("Veinte")

print("3->El diccionario es: ",diccionario)