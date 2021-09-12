'''Luego de recibir por teclado un string que contenga letras y números,imprimir la cada número contenido en el string y la suma de los mismos'''

palabra = input("Ingrese una palabra con numeros: ")
total = 0

for i in palabra:
    if (i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9'): #(i >= "0" and i<= "9") OTRA FORMA DE CONDICION!!
        print(i, " - ")
        total +=  int(i)

print("El total es: ", total)
