'''Partiendo de un string, recibir un número entero y contar cuántas palabras son mas largas, mas cortas o iguales que el número ingresado'''

frase = input("Ingrese una frase: ")
num = int(input("Ingrese un numero: "))

aux = 0
mayor = 0
menor = 0 
igual = 0

for i in frase:
    if (i != ' '):
        aux += 1 
    else:
        if(aux < num):
            menor += 1
        if(aux == num):
            igual += 1
        if(aux > num):
            mayor += 1
        aux = 0

if(aux < num):
    menor += 1
if(aux == num):
    igual += 1
if(aux > num):
    mayor += 1

print("Palabras mayores: ", mayor)
print("Palabras menores: ", menor)
print("Palabras iguales: ", igual)




