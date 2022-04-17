'''
@author: zhzj

Successione di Padovan

La successione di Padovan è la serie di numeri naturali P(n) 
definita dai valori iniziali:
P(0) = P(1) = P(2) = 1
E per tutti i valori di n > 3 dalla relazione:
P(n) = P(n-2) + P(n-3)
I primi valori della successione sono:
1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, …

Scrivere un programma che chiede all'utente un numero intero e verifica se il numero inserito (che deve essere positivo) è uno degli elementi della successione di Padovan.

'''

""" 

# versione v1.0 :

non è necessario utilizzo della ricorsione, in quanto costruzione di una serie può rendere più agevole

def padovan(n) :
    if n == 0 :
        return 1
    elif n == 1 :
        return 1
    elif n == 2 :
        return 1
    else :
        return padovan(n-2) + padovan(n-3) 
"""

# versione v1.1 : Dynamic Programming
def main() :
    n = int(input("Inserisci un numero: "))
    if n < 0 :
        print("Numero non valido. Inserisci un numero positivo.")
    else :
        # costruisco la successione di Padovan
        P = [1, 1, 1]
        i = 3
        while i < n :
            P.append(P[i-2] + P[i-3]) # che indice ha questo valore? --> [-1]
            if P[-1] > n :
                # se il valore è maggiore del numero inserito, allora non è un elemento della successione
                print(n, "non è un elemento della successione di Padovan.")
                break
            elif P[-1] == n :
                # se il valore è uguale al numero inserito, allora è un elemento della successione
                print(n, "è un elemento della successione di Padovan.")
                break
            else :
                # continua a costruire la successione
                i = i + 1

main()