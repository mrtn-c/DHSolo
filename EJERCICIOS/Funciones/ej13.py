'''Diseñar un programa que a partir de una lista genere otra con sólo losnúmeros positivos. Utilizar filter()'''

lista = [1,2,3,-4,-5,-6]

lista_re = list(filter(lambda x: x>=0, lista))

print(lista_re)