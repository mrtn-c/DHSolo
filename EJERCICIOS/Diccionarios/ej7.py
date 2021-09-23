'''A partir del diccionario del apartado anterior, generar una lista con 10 diccionarios. Cada uno de ellos representa un alumno distinto'''

estudiantes = []

for i in range(2):
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

    estudiantes.append(estudiante)

    for k in estudiantes:
        print(str(k)+"\n\n")

for k in estudiantes:
    print("Estudiante ", k, ": ", estudiantes[k])