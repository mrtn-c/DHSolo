'''solicitar el ingreso de un string por teclado junto a un número entero. 
Se deben eliminar los caracteres comprendidos el inicio del string y el número ingresado'''

str = input("Ingrese algo, con un numero: ")
cond = False
numero = ""

for i in str:
    if(i>="0" and i<="9"):
        cond=True
    if(cond):
        numero = numero + i

print(numero)