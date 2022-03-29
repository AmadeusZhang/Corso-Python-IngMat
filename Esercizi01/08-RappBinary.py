"""
Created on Sun Mar 20 22:24:41 2022

@author: zhzj

Dato un numero positivo Q, scrivere la sua rappresentazione in binario naturale, indicando anche il minimo numero di bit utilizzato.
Il programma dovrà esibire un comportamento come nell'esempio seguente:
	Input: 19 in decimale
	Output: con 5 bit = 10011 in binario.

"""

num = int( input("Inserisci un numero intero naturale in decimale: ") )

if num > 0 :
    rapp = ''
    # find the max index
    ii = 0
    while num >= 2**ii :    # attenzione: min(2^ii)=1, pertanto per num=0 ci vuole una trattazione a parte
        ii = ii+1

    max_i = ii
    ii = ii-1
    while ii >= 0 :
        if num >= 2**ii :
            rapp = rapp + '1'
            num = num - 2**ii
        else :
            rapp = rapp + '0'

        ii = ii-1

    print("con", max_i, "bit =", rapp, "in binario.")

elif num == 0 :
    print('0')
    
else :
    print("Numero non valido")

'''
To-Do: non riesce a handle with input=0 (extreme case and mayby only one)
'''