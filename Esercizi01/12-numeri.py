'''
@author: zhzj

Scrivere un programma che legge un intero positivo n da stdin e verifica se n è un numero mancante, perfetto o abbondante. 
Chiamiamo S(n) la somma di tutti i divisori propri di n (1 incluso, n escluso). 
Un numero n si dice perfetto se n = S(n), mancante se n > S(n), abbondante se n < S(n). Esempio:

10: MANCANTE
12: ABBONDANTE
28: PERFETTO 

'''

def main() :
    n = int(input("Inserisci un numero: "))
    somma = 0
    for i in range(1, n) :
        if n % i == 0 :         # se è un divisore
            somma += i
    if n == somma :
        print("Perfetto")
    elif n > somma :
        print("Mancante")
    else :
        print("Abbondante")