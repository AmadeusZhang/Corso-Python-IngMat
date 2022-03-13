"""
Scrivere un programma che dato un numero N>0 di valori da inserire da tastiera, 
stampi a video il massimo della sequenza inserita e la posizione in cui tale valore è stato inserito. 
Supponiamo, per semplicità, che non ci siano duplicati
Esempio: N=5 sequenza: 3, 2, 9, 5, 1 
	Max=9 Pos=3
"""

N = int( input("Quanti? : ") )

if N > 0 :
    cont = 1
    val = int( input("Inserisci un valore: ") )
    max = val
    pos = 1
    while cont < N :
        val = int( input("Inserisci un valore: ") )
        cont = cont + 1
        if val > max :
            max = val
            pos = cont
    
    print("Il massimo è ", max, " in posizione ", pos)

else :
    print("N<=0 non accettabile")
