'''
Si scriva un programma che letto un numero intero positivo dallo standard input, visualizzi a terminale il quadrato del numero stesso facendo uso soltanto di operazioni di somma.
Si osservi che il quadrato di ogni numero intero positivo N può essere costruito sommando tra loro i primi N numeri dispari.
Esempio: N = 5; N2 = 1 + 3 + 5 + 7 + 9 = 25. 
'''

N = int( input("Inserisci un numero intero postivivo: ") )

# controllo su N
if N > 0 :
    sq_N = 0
    
    # interpretazione errata del testo
    # for ii in range(N) :
    #     if ( ii%2 != 0 ) :  # per ii dispari
    #         sq_N = sq_N + ii
    
    ii = 0
    while ii < N :              # sommo N numeri dispari
        sq_N = sq_N + 2*ii + 1  # un numero dispari può essere espresso come 2k+1, per k = 1, ... , n
        ii = ii + 1
            
    print("N^2 = ", sq_N)
    
else :
    print("N non valido")
