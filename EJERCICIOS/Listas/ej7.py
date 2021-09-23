'''Crear una lista que contenga en su interior 27 listas, asociadas cada unaa una letra del alfabeto español.
Luego tomar por teclado 32 palabras y añadirlas cada una a la lista co-rrespondiente a su primera letra'''

lista = [[] for i in range(26)] #No toma ñ :(
    
for i in range(26):
    lista[i].append(chr(i+97))
print(lista)

for i in range(32):
    aux = input("Ingrese palabra: ")
    for z in range(26):
        if aux.startswith(lista[z][0]) == True:
            lista[z].append(aux)

print("La lista quedo asi: ",  lista)