#Triangulo de Pascal, pasando n cantidad de lineas

def trianguloPascal(n):

    lista = [[1],[1,1]]

    for i in range(1,n):

        linea = [1] #Siempre la linea empieza con un 1

        for j in range(0,len(lista[i])-1):
                                                                                    #VER ESTO HERMANO NO LO ENTIENDO
            linea.extend([lista[i][j] + lista[i][j+1]])
        
        linea += [1]
        lista.append(linea)
    
    return lista

n = int(input("Ingrese la cantidad de lineas de pascal que necesita: "))
resultado = trianguloPascal(n)


for i in resultado:
    print(i) 
