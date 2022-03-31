'''
@author: zhzj

Scrivere un programma che legge un intero positivo n da stdin e verifica se n può essere scomposto nella somma di due quadrati (verifica cioè se esistone a, b | a^2+b^2=n ). 
Se sì, stampare a video la scomposizione. 

Esempi:
2 ==> 2 = 1 + 1 = 1^2 + 1^2
28 ==> NON SCOMPONIBILE
145 ==> 146 = 25 + 121 = 5^2 + 11^2

'''

def main() :
    n = int(input("Inserisci un numero: "))
    for i in range(1, n) :
        for j in range(1, n) :
            if i**2 + j**2 == n :
                print(n, "=", i, "^2 +", j, "^2")
                return
    
    print("NON SCOMPONIBILE")

main() # chiamata della funzione principale

'''
Variante: mostrare tutte le possibili scomposizioni

e.g. 50
'''
