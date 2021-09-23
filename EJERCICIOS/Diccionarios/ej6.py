'''Modificar el ejercicio anterior para que la lista de materias de cursa ahora sea un diccionario. Es decir, cada materia tiene asociado un código'''

materia = dict()
estudiante = {'Nombre':'', 'Apellido':'', 'Legajo':'', 'Materias':materia}

estudiante['Nombre']=input("Ingrese el nombre: ")
estudiante['Apellido']=input("Ingrese el apellido: ")
estudiante['Legajo']=input("Ingrese el legajo: ")

while True:
    aux = input("Ingrese la materia: ")
    if aux == '.':
        break
    materia[aux]=input("ingrese el codigo de la materia: ")

estudiante['Materias']=materia

print("El estudiante quedo: ", estudiante)