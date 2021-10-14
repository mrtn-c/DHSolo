'''Diseñar un programa que sume tres listas. Utilizar map() y lambdas.'''

lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = [1,2,3,4,5,6,7,8,9,10]
lista3 = [1,2,3,4,5,6,7,8,9,10]

resultado = list(map(lambda x,y,z: x+y+z, lista,lista2,lista3  ))

print(resultado)