#Escribir una función que reciba un string y luego calcule y retorne la cantidad de letras mayúsculas y minúsculas presentes en la misma

def mayusculasMinusculas(palabra):
    mayusculas = 0
    minusculas = 0

    for i in palabra:
        if (i>='a' and i<='z'):
            minusculas+=1
        if (i>='A' and i<='Z'):
            mayusculas+=1
    
    return mayusculas,minusculas

palabra = input("Ingrese una palabra: ")
mayusculas,minusculas = mayusculasMinusculas(palabra)

print("La cantidad de mayusculasculas es: ", mayusculas, " y la cantidad de minusculasculas: ", minusculas)
