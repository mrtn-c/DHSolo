/*rear un código fuente en C que sume dos números enteros recibidos porteclado e imprima el resultado por pantalla.Luego, 
sobre el ejemplo anterior:Obtener el archivo luego de la ejecución del pre-procesador. ¿Quédirectivas son eliminadas o reemplazas?
A partir del item anterior, obtener el código assembler utilizando GCC. 
¿Para qué arquitecutura es el código?Ejecutar el ensamblado del apartado anteriorEnlazar el objeto y generar el ejecutable*/

#include <stdio.h>

int main(){

    int num1, num2, suma;

    printf("Ingrese un numero: ");
    scanf("%d", &num1);
    
    printf("Ingrese otro numero: ");
    scanf("%d", &num2);
    
    suma = num1 + num2;
    
    printf("El resultado fue: %d", suma);
    
    return 0;

}