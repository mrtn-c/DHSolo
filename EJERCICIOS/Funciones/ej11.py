'''Diseñar un programa calcule la raíz cuadrada de cada elemento de una lista. Utilizar map()'''

def raiz(x):
    return x*x

lista = [1,2,3,4]

resultado = list(map(raiz,lista))

print(resultado)
