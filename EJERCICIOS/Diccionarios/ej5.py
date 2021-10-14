'''A partir del diccionario del ejercicio anterior, modificar el número de legajo y agregar dos materias nuevas en la lista de materias'''

lista = []
estudiante = {'Nombre':'', 'Apellido':'', 'Legajo':'', 'Materias':''}

print("Ingrese los datos del estudiante: ")
for i in estudiante:
    print(i, ":", end=' ')
    aux = input()
    estudiante[i] = aux

estudiante['Materias'] = estudiante['Materias'].split(', ')

print("El original: ",estudiante)

estudiante['Legajo']=input("Ingrese legajo: ")
estudiante['Materias'].append(input("Ingrese la nueva materia: "))
estudiante['Materias'].append(input("Ingrese la otra materia: "))

print("Estudiante nuevo mas estudioso: ", estudiante)