'''Recibir por teclado una frase de más de 80 caracteres. 
Luego, recibir tam-bién una segunda palabra. Finalmente, imprimir cuantas veces aparece lasegunda palabra en la frase del comienzo'''

frase = ""
while (len(frase) < 80):
    frase = input("Ingrese una frase de mas de 80 caracteres\n")

palabra = input("Ingrese la palabra a buscar: ")
print("La palabra ", palabra, "se encuentra en la frase ", frase.count(palabra), "veces")