#Escribir un programa que partiendo de una lista de números enteros, los
# clasifique en dos listas distintas: una con los números pares y otra con los
# impares. Resolver utilizando lambdas

lista = [1,2,3,4,5,6,7,8,9,10]

lista_par = [x for x in lista if x%2 == 0]

print(lista_par)

lista_impar = [x for x in lista if x%2 != 0]

print(lista_impar)




