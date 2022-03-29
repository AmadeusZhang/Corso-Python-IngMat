"""
Created on Thu Mar 17 22:11:14 2022

@author: zhzj

Scrivere un programma in grado di acquisire in ingresso dall'utente un valore intero positivo num.
Il programma deve stampare a video tutti i fattori primi di num. 

"""

# Acquisizione di un intero positivo
num = int( input("Inseisci un valore intero positivo: ") )

div = 2

while ( div <= num ) :
    if ( num%div == 0 ) :
        num = num/div               # aggiorno dividendo
        print(div, end=" ")
    
    else :
        div = div + 1;
