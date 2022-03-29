"""
Created on Thu Mar 17 22:37:35 2022

@author: zhzj

Si definisce Triangolare un numero costituito dalla somma dei primi N numeri interi positivi per un certo N.
Ad esempio: per Q = 10 si ha Q =1+2+3+4, da cui N = 4.

Scrivere un programma che stabilisca se un numero intero positivo Q, letto dallo standard input, è un numero triangolare o meno, 
utilizzando soltanto operazioni tra numeri interi. In caso affermativo stampare a video il numero inserito e il massimo degli addendi che lo compongono.

"""

# Lettura di un numero intero positivo
Q = int( input("Inserisci un numero intero positivo: ") )

# stabilire se Q è triangolare: esiste un N tale che Q = SUM(1:N)
N = 1
while ( N < Q ) :
    somma = 0
    for ii in range(N+1) :            # N is not included in range()
        somma = somma + ii
    
    if ( somma == Q ) :
        print("Q: ", Q, " N: ", N)
        break
    
    N = N + 1