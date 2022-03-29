# -*- coding: utf-8 -*-
"""
Python per Ingegneria Matematica - Lezione 0
"""

print("Ciao mondo")

# pint("op")

"""
Python è un linguaggio interpretato, e non compilato come C, pertanto nonostante
ci siano errori di sintassi il programma comunque lo esegua
"""

a = 5
print(a)
a = "CIAO"
print(a)

# Python è a variabile dinamico


# Chiede due interi e li somma, poi stampa la somma
a = int( input("Inserire un intero: ") ) 
"""
input() restituisce una stringa (nonostante sia inserito un numero intero)
int() converte in intero quanto restituito da input
print(a)
"""

b = int( input("Inserire un intero: ") )
ris = a+b
print(ris)

# se solo uno dei due ha int(), non si potrà eseguire l'operazione di somma
# se invece non si ha nessuno l'int(), si esegue una concatenazione

a = 5
b = 2
print(a+b, a-b, a*b, a/b, a//b, a%b, a**b)

# Novità: // divisione tra interi, % resto della //

n = int( input("Inserire un intero: ") )

if n>0:
    print("positivo")
elif n==0:
    print("nullo")
else:
    print("negativo")
    
while n>0:
    print("Meno ", n)
    n = n-1
print("VAI!")

# MCD, mcm
a = int( input("Inserire un intero: ") )
b = int( input("Inserire un intero: ") )

mcd = 1

if a>b:
    min=b
else:
    min=a

x = 2

while x < min:
    if a % x == 0 and b % x == 0 :
        mcd = x
        # x = x+1    il programma va in infinite loop
    x = x+1
        
print(mcd)

# Algoritmo di Eulero
mcd = 1
x = 2
while a!=b :
    if a>b:
        a=a-b
    else:
        b=b-a

print(a)

# Ricevere delle sequenze di interi positivi terminati da 0
# stampava la somma delle sequenze, al "-1" si fermava
val = 0
somma = 0
val = int(input("Inserire un valore: "))
while val != -1 :
    # Calcolare una somma di sequenza
    while val != 0 and val != -1:
        somma = somma + val
        val = int(input("Inserire un valore: "))
    # Stamparla
    print(somma)
    somma = 0
    if val != -1 :
        val = int(input("Inserire un valore: "))
    
    
# Libreria random - Calcolo Pi-greco
import random
N = int( 1e6 )
target = 0
i = 0
while i < N :
    x = random.random()
    y = random.random()
    if (( x**2 + y**2 )**(1/2)) <= 1 :
        target = target + 1
    i = i + 1

pi = 4*(target/N)
print(pi)

