"""
Created on Thu Mar 17 08:14:50 2022

@author: zhzj

Si scriva un programma che legge una sequenza di interi positivi (la sequenza termina quando viene inserito il valore -1),
conta il numero complessivo dei numeri che sono multipli di 3, di 5 oppure di 7 compresi nella sequenza e stampa questo valore. 
Per esempio, nel caso la sequenza in ingresso fosse "4 8 12 15 14 8", il programma dovrebbe stampare il valore 3. 


"""
c = int(input("Inserisci una sequenza di interi positivi che termina con -1: "))
cont = 0
while ( c != -1 ):
    if ( c%3 == 0 or c%5 == 0 or c%7 == 0 ):
        cont = cont + 1
        
    c = int(input())

print("Valore: ", cont)