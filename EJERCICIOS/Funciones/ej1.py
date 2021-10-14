#Crear una función en Python que imprima el valor y el ID de un objetorecibido en la misma. Luego crear un objeto lista, un entero y una tupla.
# Finalmente se deben imprimir estos tres objetos utilizando la función ysin hacerlo.
# Extraer conclusiones sobre como las funciones en Python reciben paráme-tros.

def imprimir(aux):
    print("El valor es: ", str(aux), " y su ID es: ", str(id(aux)))

lista = [1,2,3,4,5]
entero = 2
tupla = (1,2,3)

#Con funcion
imprimir(lista)
imprimir(entero)
imprimir(tupla)
#Sin Funcion
print("El valor es: ", str(lista), " y su ID es: ", str(id(lista)))
print("El valor es: ", str(entero), " y su ID es: ", str(id(entero)))
print("El valor es: ", str(tupla), " y su ID es: ", str(id(tupla)))
