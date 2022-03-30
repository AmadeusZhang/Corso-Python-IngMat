'''
@author: zhzj

Su una scacchiera 8x8 sono posizionati due pezzi: il Re bianco e la Regina nera.
Si scriva un programma che, acquisite le posizioni del Re e della Regina, determini se la Regina è in posizione tale da poter mangiare il Re.
Le posizioni dei due pezzi sono identiﬁcate da mediante la riga e la colonna su cui si trovano, espresse come numeri interi tra 1 e 8.
'''

def main() :
    print("Inserisci la posizione del Re:")
    r = int(input("Riga: "))
    if r < 1 or r > 8 :
        print("Riga non valida")
        return
    c = int(input("Colonna: "))
    if c < 1 or c > 8 :
        print("Colonna non valida")
        return

    print("Inserisci la posizione della Regina:")
    r1 = int(input("Riga: "))
    if r1 < 1 or r1 > 8 :
        print("Riga non valida")
        return
    c1 = int(input("Colonna: "))
    if c1 < 1 or c1 > 8 :
        print("Colonna non valida")
        return

    if r == r1 or c == c1 :         # Se le righe o le colonne sono uguali allora il Re è sotto la Regina
        print("La Regina è in posizione di mangiare il Re.")
    elif r-r1 == c-c1 :             # Devo controllare anche le diagonali
        print("La Regina è in posizione di mangiare il Re.")
    else :
        print("La Regina non è in posizione di mangiare il Re.")

main()