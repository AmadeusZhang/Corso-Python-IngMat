"""
@author: zhzj

Si realizzi un programma per risolvere equazioni di secondo grado.

In particolare, data una generica equazione di secondo grado nella forma
ax2 + bx + c = 0
dove a, b, c sono coefﬁcienti reali noti e x rappresenta l'incognita, il programma determini le due radici x1 ed x2 dell'equazione data, ove esse esistano.

Si identiﬁchino tutti i casi particolari (a = 0, b= 0, c=0) e si stampino gli opportuni messaggi informativi.

"""

def main() :
    # Inserimento di una tripletta di coefficienti
    a = float(input("Inserisci il coefficiente a: "))
    b = float(input("Inserisci il coefficiente b: "))
    c = float(input("Inserisci il coefficiente c: "))
    
    # controllo validità dei coefficienti
    if a < 0 or b < 0 or c < 0 :
        print("Coefficienti non validi.")
        return
    
    # calcolo delle radici
    delta = b**2 - 4*a*c
    if delta < 0 :
        print("L'equazione non ha radici reali.")
    elif delta == 0 :
        x1 = -b/(2*a)
        print("L'equazione ha una sola radice reale con molteplitcità 2:", x1)
    else :
        x1 = (-b + delta**0.5)/(2*a)
        x2 = (-b - delta**0.5)/(2*a)
        print("L'equazione ha due radici reali:", x1, "e", x2)

main()