"""
Created on Thu Mar 17 22:03:41 2022

@author: zhzj


Scrivere un programma in grado di acquisire in ingresso dall'utente un valore intero num e una sequenza di interi che termina con uno 0 (zero).
Il programma deve stampare a video il numero di valori pari nella sequenza che sono divisori di num. 
0 viene considerato come valore sentinella. 
"""

# acquisizione di un valore intero
num = int( input("Inserisci un valore intero: ") )
cont = 0

# acquisizione di una sequenza di interi che termina con 0 (zero)
c = int( input("Inserci una sequenza di interi: ") )
while ( c != 0 ) :
    # stabilire se sono divisibili per num
    if ( c % num == 0 ) :
        cont = cont + 1
    
    c = int( input() )
    
print("Sono: ", cont)