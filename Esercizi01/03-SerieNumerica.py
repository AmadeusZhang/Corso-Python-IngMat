"""
Created on Wed Mar 16 23:30:10 2022

@author: zhzj

Scrivere i primi N (con N chiesto all'utente) elementi di una serie così definita: 
i primi tre elementi valgono 1, i successivi (i>=4) valgono la somma degli elementi i-1 e i-3 
1 1 1 2 3 4 6 9 13 19 28 41 60 …

"""

N = int(input("Inserisci un numero intero: "))

if N > 0 :
    serie = [1, 1, 1]
    ii = 3
    while ii < N :
        serie.append(serie[ii-1]+serie[ii-3])
        ii = ii+1
    
    print("Serie: ", serie)

else :
    print("N non valido")
