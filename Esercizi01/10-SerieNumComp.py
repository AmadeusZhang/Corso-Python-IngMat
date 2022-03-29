"""
Created on Fri Mar 25 22:43:42 2022

@author: zhzj

Scrivere un programma che stampa i primi 20 numeri altamente composti. 
Un numero altamente composto è tale che qualunque numero minore di esso ha meno divisori.
I primi numeri altamente composti sono 1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 10080

"""

# definisco una funzione che mi ritorna numeri divisori di un numero
def num_div(n) :
    ii = 1
    cont = 0
    while ii < n :
        if n % ii == 0 :
            cont = cont+1
        
        ii = ii+1
    
    return cont

# stampa primi 20 numeri
contatori = 0
n = 1
while contatori < 20 :
    ii = 1
    while ii < n :
        if num_div(n) < num_div(ii) :
            contatori = contatori+1
            break
        
        ii = ii+1
    
    
        
        