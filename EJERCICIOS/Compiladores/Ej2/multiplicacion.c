#include "multiplicacion.h"

void multiplicacion(int numeros1[10],int numeros2[10], int resultado[10]){

    for (int j=0; j<10; j++){
        resultado[j] = numeros1[j] * numeros2[j];
    }

}