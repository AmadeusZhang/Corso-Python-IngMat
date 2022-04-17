'''
@author: zhzj

Scrivere un programma che legge da stdin una sequenza (di lunghezza arbitraria) di numeri interi positivi, terminata da 0, e indica, alla fine della sequenza, qual è la lunghezza della massima sottosequenza di numeri consecutivi in ordine crescente. Esempi:

13  3  8  4  5  1 17  0
Lung. max = 2

21  19  18  14  9  6  4  3 0
Lung. max = 1

2  1  3  6  8  5  1 12 18 17  0
Lung. max = 4

'''

def main() :
    num = int(input("Inserisci un numero: "))
    prec = num
    cont = 1
    max = 0
    while num != 0 :
        if num > 0 :
            if (num > prec) :
                cont += 1
            else :
                if cont > max :
                    max = cont
                cont = 1
        else :
            print("Numero non valido. Inserisci un numero positivo.")

        prec = num
        num = int(input("Inserisci un numero: "))
    
    print("La massima lunghezza consecutiva è: ", max)

main()