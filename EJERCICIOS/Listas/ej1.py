'''Considerando dos listas de números enteros
- Calcular e imprimir la suma vectorial de ambas
- Calcular e imprimir el producto punto
- De cada una de las listas imprimir los números divisibles por 5'''

def cargarLista():

    lista = []
    aux = 0
    
    while True:
        aux = input("Ingrese un numero: ")
        if (aux >= '0' and aux <= '9'):
            lista.append(int(aux))
        else:
            break
    
    return lista

def divisible(lista):

    print("Numeros divisibles por 5: ")

    for i in lista:
        if ((i % 5) == 0):
            print(". ", i)

def sumaYProducto(lista1, lista2):
    suma = 0
    producto_aux = 0
    producto_punto = 0
    cont = 1
    tamMen = 0

    if (len(lista1)<len(lista2)):
        tamMen = len(lista1)
    else:
        tamMen = len(lista2)

    print("La suma vectorial es: \n")
    for i in range(tamMen):
        suma = lista1[i] + lista2[i]
        print(cont, ": ", suma)
        cont += 1
        producto_aux = lista1[i] * lista2[i]
        producto_punto += producto_aux
    
    print("El resultado del producto punto es: ", producto_punto)

print("Lista 1: \n")
lista1 = cargarLista()
print("Lista 2: \n")
lista2 = cargarLista()

divisible(lista1)
divisible(lista2)

sumaYProducto(lista1,lista2)


