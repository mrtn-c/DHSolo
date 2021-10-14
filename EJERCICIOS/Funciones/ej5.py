#Escribir una función que acepte parámetros posicionales y kwargs. 
#Luego la función debe imprimirlos indicando cómo fue recibido cada uno de los parámetros

def funcion(*args, **kwargs):
    
    j = 1
    for i in args:
        print("El ", j,  " valor de args es: ", str(i))
        j+=1
    
    j = 1
    for z in kwargs:
        print("El ", j,  " key de kwargs es: ", str(z), "y su valor: ", kwargs.get(z))
        j+=1

funcion(1,2,3,4,c=3,x=10)
funcion(2,3,4,x=3,z=2,d='jaja')

