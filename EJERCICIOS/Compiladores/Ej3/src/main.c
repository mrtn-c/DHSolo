/*Generar programas en C que realicen las siguientes operaciones arreglosde números enteros utilizando aritmética de punteros. 
En el caso de opera-ciones, se deben utilizar dos arreglos de igual longitud y el resultado debe 
almacenarse en un tercer arreglo:Sumar Restar Multiplicar Buscar máximo Buscar mínimo Cada una de estas funciones debe implementarse en un archivo distinto.
Generar un main donde las funciones creadas anteriormente sean llamada y ejecutar una compilación de dos pasos cada vez que sea necesario*/

#include <stdio.h>
#include <stdlib.h>
#include "sumar.h" 
//#include "multiplicacion.h"

int main(){

    int numeros1[10] = {1,2,3,4,5,6,7,8,9,10};
    int numeros2[10] = {1,2,3,4,5,6,7,8,9,10};
    int resultado[10];

    sumar(numeros1,numeros2,resultado);
    //restar(numeros1, numeros2, resultado);
    //multiplicacion(numeros1,numeros2,resultado);

    for (int i=0; i<10; i++){
        printf("%d - ", resultado[i]);
    }

    return 0;
    
}