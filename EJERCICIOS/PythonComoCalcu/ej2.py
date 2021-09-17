'''Realizar un programa que calcule el desglose mínimo en billetes y monedasde una cantidad exacta de pesos.
 Hay billetes de$1000,$500,$200,$100 y monedas de $10, $5 y $2 y $1. El desglose se realiza del más grandeal más pequeño. .
  El desglose se realiza del más grande al más pequeño.'''

monto = int(input("Ingrese el monto a abonar: "))
dinero = monto
quinientos = 0
mil = 0
doscientos = 0
cien = 0
diez = 0
cinco = 0
dos = 0
uno = 0

while(dinero != 0):
    
    if(dinero >= 1000):
        dinero = dinero - 1000
        mil+= 1
    elif(dinero >= 500):
        dinero = dinero - 500
        quinientos+= 1
    elif(dinero >= 200):
        dinero = dinero - 200
        doscientos+= 1
    elif(dinero >= 100):
        dinero = dinero - 100
        cien+= 1
    elif(dinero >= 10):
        dinero = dinero - 10
        diez+= 1
    elif(dinero >= 5):
        dinero = dinero - 5
        cinco+= 1
    elif(dinero >= 2):
        dinero = dinero - 2
        dos+= 1
    elif(dinero >= 1):
        dinero = dinero - 1
        uno+= 1 
    elif(dinero == 0):
        break;

print("Su monto se puede desglosar en: \nmil: ", mil, "\nquinientos: ", quinientos, "\ndoscientos: ", 
    doscientos, "\ncien: ", cien, "\ndiez: ", diez, "\ncinco: ", cinco,"\ndos: ", dos,"\nuno: ", uno )