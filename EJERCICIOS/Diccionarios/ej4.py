'''Crear un diccionario llamado estudiante y luego la siguiente 
estructura:Nombre: string
Apellido: stringLegajo: string
Materias que cursa: lista de strings
Cargar valores e imprimirlo por pantalla'''

lista = []
estudiante = {'Nombre':'', 'Apellido':'', 'Legajo':'', 'Materias':''}

print("Ingrese los datos del estudiante: ")
for i in estudiante:
    print(i, ":", end=' ')
    aux = input()
    estudiante[i] = aux

estudiante['Materias'] = estudiante['Materias'].split()

print(estudiante)